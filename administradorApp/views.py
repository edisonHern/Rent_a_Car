from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from core.models import Auto, Cliente, Reserva, Factura, Politica, Nosotros
from administradorApp.forms import AutoForm, ClienteForm, ReservaForm, FacturaForm, PoliticaForm, NosotrosForm, TrabajadorForm, RegistroAdministradorForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from administradorApp.decorators import administrador_required
from django.contrib.auth import get_user_model
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.core.paginator import Paginator
import datetime
from django.db.models import Sum
import pandas as pd
from django.utils.timezone import now






def login_administrador(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.tipo_usuario == 'administrador' and user.is_staff:  # Verifica el rol
                login(request, user)
                return redirect('adm_lista_autos')  # Redirige al dashboard del administrador
            else:
                messages.error(request, "No tienes permisos de administrador.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login/login_administrador.html', {'form': form})

def logout_administrador(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('carrusel_imagen')   # Redirige al login de administrador


@login_required
@administrador_required
def adm_index(request):
    
    # Obtener métricas de autos
    # Obtener métricas de autos
    total_autos = Auto.objects.count()
    autos_gasolina = Auto.objects.filter(combustible='gasolina').count()  
    autos_diesel = Auto.objects.filter(combustible='diesel').count()  
    autos_electricos = Auto.objects.filter(combustible='electrico').count()

    autos_disponibles = Auto.objects.filter(estado_auto='disponible').count()
    autos_reservados = Auto.objects.filter(estado_auto='reservado').count()
    autos_rentados = Auto.objects.filter(estado_auto='rentado').count()
    autos_mantenimiento = Auto.objects.filter(estado_auto='mantenimiento').count()

    # Obtener métricas de clientes
    total_clientes = Cliente.objects.count()
    clientes_inactivos = Cliente.objects.filter(estado_cliente='inactivo').count()
    clientes_con_reserva = Cliente.objects.filter(estado_cliente='con_reserva').count()
    clientes_rentando = Cliente.objects.filter(estado_cliente='rentando').count()

    # Obtener métricas de reservas
    total_reservas = Reserva.objects.count()  
    reservas_activas = Reserva.objects.filter(estado_reserva='activa').count()
    reservas_pagadas = Reserva.objects.filter(estado_reserva='pagada').count()
    reservas_completadas = Reserva.objects.filter(estado_reserva='completada').count()
    reservas_canceladas = Reserva.objects.filter(estado_reserva='cancelada').count()
    
    # Obtener total de facturas y monto total de ingresos  
    total_facturas = Factura.objects.count()  
    total_ingresos = Factura.objects.aggregate(Sum('total'))['total__sum'] or 0

    pagos_efectivo = Factura.objects.filter(metodo_pago='Efectivo').count()  
    pagos_debito = Factura.objects.filter(metodo_pago='Tarjeta Debito').count()  
    pagos_credito = Factura.objects.filter(metodo_pago='Tarjeta Crédito').count()

    # Obtener total de facturas del mes actual

    primer_dia_mes = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    facturas_mes = Factura.objects.filter(fecha_emision__gte=primer_dia_mes).count()

    context = {
        'total_autos': total_autos,  
        'total_clientes': total_clientes,  
        'total_reservas': total_reservas,  
        'total_facturas': total_facturas,  
        'total_ingresos': total_ingresos,

        'autos': {
            'gasolina': autos_gasolina,  
            'diesel': autos_diesel,  
            'electricos': autos_electricos,  
            'disponibles': autos_disponibles,
            'reservados': autos_reservados,
            'rentados': autos_rentados,
            'mantenimiento': autos_mantenimiento,
        },
        'clientes': {
            'inactivos': clientes_inactivos,
            'con_reserva': clientes_con_reserva,
            'rentando': clientes_rentando,
        },
        'reservas': {
            'activas': reservas_activas,
            'pagadas': reservas_pagadas,
            'completadas': reservas_completadas,
            'canceladas': reservas_canceladas,
        },




        'facturas': {
        'total_facturas': total_facturas,
        'total_mes': facturas_mes,
        },
        'pagos': {  
            'efectivo': pagos_efectivo,  
            'debito': pagos_debito,  
            'credito': pagos_credito,  
        },
    }

    return render(request, 'menu/adm_index.html', context)



#Vistas para autos
@login_required
@administrador_required
def adm_lista_autos(request):
    query = request.GET.get('q')  # Término de búsqueda
    tipo_busqueda = request.GET.get('tipo_busqueda')  # Tipo de búsqueda seleccionado
    estado_auto = request.GET.get('estado')  # Filtro por estado

    autos = Auto.objects.all()
    paginator = Paginator(autos, 20)  # 20 autos por página
    page_number = request.GET.get('page')  # Obtener el número de página de la URL
    page_obj = paginator.get_page(page_number)

    # Filtrar según el tipo de búsqueda seleccionado
    if query:
        if tipo_busqueda == 'patente':
            autos = autos.filter(patente__icontains=query)
        elif tipo_busqueda == 'marca':
            autos = autos.filter(marca__icontains=query)
        elif tipo_busqueda == 'modelo':
            autos = autos.filter(modelo__icontains=query)
        elif tipo_busqueda == 'año':
            autos = autos.filter(año__icontains=query)
        elif tipo_busqueda == 'kilometraje':
            autos = autos.filter(kilometraje__icontains=query)
        elif tipo_busqueda == 'combustible':
            autos = autos.filter(combustible__icontains=query)
        elif tipo_busqueda == 'color':
            autos = autos.filter(color__icontains=query)
        elif tipo_busqueda == 'puertas':
            autos = autos.filter(puertas__icontains=query)
    if estado_auto:
        autos = autos.filter(estado_auto=estado_auto)
    return render(request, 'auto/adm_lista_autos.html', {'autos': autos, 'page_obj': page_obj})

@login_required
@administrador_required
def detalle_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    return render(request, 'auto/adm_detalle_auto.html', {'auto': auto})

@login_required
@administrador_required
def ingresar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('adm_lista_autos')
    else:
        form = AutoForm()
    return render(request, 'auto/adm_ingresar_auto.html', {'form': form})

@login_required
@administrador_required
def modificar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        form = AutoForm(request.POST, request.FILES, instance=auto,)
        if form.is_valid():
            form.save()
            return redirect('adm_lista_autos')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'auto/adm_modificar_auto.html', {'form': form})

@login_required
@administrador_required
def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('adm_lista_autos')
    return render(request, 'auto/adm_eliminar_auto.html', {'auto': auto})





#Vistas para clientes
@login_required
@administrador_required
def adm_lista_clientes(request):
    query = request.GET.get('q')  # Término de búsqueda
    tipo_busqueda = request.GET.get('tipo_busqueda')  # Tipo de búsqueda seleccionado
    estado_cliente = request.GET.get('estado')  # Filtro por estado

    clientes = Cliente.objects.all()

    # Filtrar según el tipo de búsqueda seleccionado
    if query:
        if tipo_busqueda == 'rut':
            clientes = clientes.filter(rut__icontains=query)
        elif tipo_busqueda == 'nombre':
            clientes = clientes.filter(nombre__icontains=query)
        elif tipo_busqueda == 'apellido':
            clientes = clientes.filter(apellido__icontains=query)
        elif tipo_busqueda == 'licencia':
            clientes = clientes.filter(licencia_conducir__icontains=query)
    if estado_cliente:
        clientes = clientes.filter(estado_cliente=estado_cliente)

    return render(request, 'cliente/adm_lista_clientes.html', {'clientes': clientes})

@login_required
@administrador_required
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/adm_detalle_cliente.html', {'cliente': cliente})

@login_required
@administrador_required
def ingresar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cliente = form.save()
            return redirect('adm_detalle_cliente', cliente_id=cliente.id)
    else:
        form = ClienteForm()
    return render(request, 'cliente/adm_ingresar_cliente.html', {'form': form})

@login_required
@administrador_required
def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('adm_lista_clientes')  
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente/adm_modificar_cliente.html', {'form': form})

@login_required
@administrador_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id= cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('adm_lista_clientes')
    return render(request, 'cliente/adm_eliminar_cliente.html', {'cliente': cliente})




#Vistas para reservas
@login_required
@administrador_required
def lista_reservas(request):    
    query = request.GET.get('q')  # Término de búsqueda
    tipo_busqueda = request.GET.get('tipo_busqueda')  # Tipo de búsqueda seleccionado
    estado_reserva = request.GET.get('estado')  # Filtro por estado

    reservas = Reserva.objects.all()
    for reserva in reservas:
        reserva.verificar_estado_reserva()

    # Filtrar según el tipo de búsqueda seleccionado
    if query:
        if tipo_busqueda == 'codigo_reserva':
            reservas = reservas.filter(codigo_reserva__icontains=query)
        elif tipo_busqueda == 'patente':
            reservas = reservas.filter(auto__patente__icontains=query)
        elif tipo_busqueda == 'rut':
            reservas = reservas.filter(cliente__rut__icontains=query)
        
    if estado_reserva:
        reservas = reservas.filter(estado_reserva=estado_reserva)

    return render(request, 'reserva/adm_lista_reservas.html', {'reservas': reservas})

@login_required
@administrador_required
def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'reserva/adm_detalle_reserva.html', {'reserva': reserva})

@login_required
@administrador_required
def ingresar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        
        if form.is_valid():
            # Obtener el auto seleccionado en el formulario
            auto = form.cleaned_data['auto']
            
            # Verificar si el auto ya está reservado o rentado
            if auto.estado_auto in ['reservado', 'rentado']:
                messages.error(request, 'Este auto ya está reservado o rentado.')
                form.add_error('auto', 'Este auto ya está reservado o rentado.')
                return render(request, 'reserva/ingresar_reserva.html', {'form': form})

            # Si el auto está disponible, crear la reserva
            reserva = form.save(commit=False)  # Crea la reserva sin guardarla en la base de datos
            #reserva.estado_reserva = 'activa'  # Establecer el estado inicial de la reserva
            reserva.save()  # Guardar la reserva en la base de datos


            # Actualizar el estado del auto y cliente según el estado de la reserva
            if reserva.estado_reserva == 'activa':
                reserva.auto.cambiar_estado('reservado')
                reserva.cliente.cambiar_estado('con_reserva')
            elif reserva.estado_reserva == 'cancelada':
                reserva.auto.cambiar_estado('disponible')
                reserva.cliente.cambiar_estado('inactivo')
            elif reserva.estado_reserva == 'completada':
                reserva.auto.cambiar_estado('disponible')
                reserva.cliente.cambiar_estado('inactivo')

            reserva.auto.save()
            reserva.cliente.save()

            messages.success(request, 'Reserva creada con éxito.')

            # Redirigir a la lista de reservas
            return redirect('adm_lista_reservas')
        
        else:
            # Si el formulario no es válido
            messages.error(request, 'Hubo un error al crear la reserva.')

    else:
        form = ReservaForm()


    return render(request, 'reserva/adm_ingresar_reserva.html', {'form': form})

@login_required
@administrador_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)  
        if form.is_valid():
            form.save()
            
            # Actualizar el estado del auto y cliente según el estado de la reserva
            if reserva.estado_reserva == 'activa':
                reserva.auto.cambiar_estado('reservado')
                reserva.cliente.cambiar_estado('con_reserva')
            elif reserva.estado_reserva == 'cancelada':
                reserva.auto.cambiar_estado('disponible')
                reserva.cliente.cambiar_estado('inactivo')
            elif reserva.estado_reserva == 'completada':
                reserva.auto.cambiar_estado('disponible')
                reserva.cliente.cambiar_estado('inactivo')

            reserva.auto.save()
            reserva.cliente.save()

            return redirect('adm_lista_reservas')  
    else:
        form = ReservaForm(instance=reserva)
    
    return render(request, 'reserva/adm_modificar_reserva.html', {'form': form})



@login_required
@administrador_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    try:
        # Obtener el auto y cliente de la reserva
        auto = reserva.auto
        cliente = reserva.cliente

        # Verificar si el auto tiene otras reservas activas
        otras_reservas_activas = Reserva.objects.filter(
            auto=auto,
            estado_reserva='activa'
        ).exclude(id=reserva_id).exists()

        # Solo cambiar el estado del auto si no tiene otras reservas activas
        if not otras_reservas_activas:
            auto.estado_auto = 'disponible'
            auto.save()

        # Verificar si el cliente tiene otras reservas activas
        otras_reservas_cliente = Reserva.objects.filter(
            cliente=cliente,
            estado_reserva='activa'
        ).exclude(id=reserva_id).exists()

        # Solo cambiar el estado del cliente si no tiene otras reservas activas
        if not otras_reservas_cliente:
            cliente.estado_cliente = 'inactivo'
            cliente.save()

        # Eliminar la reserva
        reserva.delete()

        messages.success(request, 'Reserva eliminada exitosamente.')

    except Exception as e:
        messages.error(request, f'Error al eliminar la reserva: {str(e)}')

    return redirect('adm_lista_reservas')


@login_required
@administrador_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if reserva.estado_reserva in ['activa', 'pagada']:
        reserva.estado_reserva = 'cancelada'
        reserva.verificar_estado_reserva()
        messages.success(request, 'La reserva ha sido cancelada exitosamente.')
    else:
        messages.error(request, 'No se puede cancelar una reserva que ya está completada o cancelada.')

    return redirect('adm_lista_reservas')















#Vista para facturas
@login_required
@administrador_required
def lista_facturas(request):
    

    query = request.GET.get('q')  # Término de búsqueda
    tipo_busqueda = request.GET.get('tipo_busqueda')  # Tipo de búsqueda seleccionado (por ejemplo: código factura, código reserva, etc.)
    estado_factura = request.GET.get('estado')  # Filtro por estado de la factura (si aplica)

    facturas = Factura.objects.all()

    # Filtrar según el tipo de búsqueda seleccionado
    if query:
        if tipo_busqueda == 'codigo_factura':
            facturas = facturas.filter(codigo_factura__icontains=query)
        elif tipo_busqueda == 'codigo_reserva':
            facturas = facturas.filter(reserva__codigo_reserva__icontains=query)
        elif tipo_busqueda == 'rut_cliente':
            facturas = facturas.filter(cliente__rut__icontains=query)
    
    # Filtrar por estado (si aplica)
    if estado_factura:
        facturas = facturas.filter(estado=estado_factura)

    return render(request, 'factura/adm_lista_facturas.html', {'facturas': facturas})

@login_required
@administrador_required
def detalle_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    return render(request, 'factura/adm_detalle_factura.html', {'factura': factura})


@login_required
@administrador_required
def ingresar_factura(request):
    if request.method == 'POST':
        form = FacturaForm(request.POST)
        if form.is_valid():
            reserva = form.cleaned_data['reserva']
            cliente = reserva.cliente
            auto = reserva.auto

            # Crear la factura
            factura = form.save(commit=False)
            factura.cliente = cliente
            factura.reserva = reserva
            factura.save()

            #Actualizar estados manualmente
            reserva.estado_reserva = 'pagada'
            auto.cambiar_estado('rentado')
            cliente.cambiar_estado('rentando')

            # Guardar los cambios
            reserva.save()
            auto.save()
            cliente.save()

            messages.success(request, 'Factura creada exitosamente y estados actualizados.')
            return redirect('adm_lista_facturas')
        else:
            messages.error(request, 'Hubo un error al crear la factura. Verifique los datos ingresados.')
    else:
        form = FacturaForm()

    return render(request, 'factura/adm_ingresar_factura.html', {'form': form})

@login_required
@administrador_required
def generar_factura_desde_reserva(request, reserva_id):

    # Obtener la reserva desde la base de datos
    reserva = get_object_or_404(Reserva, id=reserva_id)
    cliente = reserva.cliente
    auto = reserva.auto

    # Verificar si la reserva ya tiene una factura asociada
    if reserva.factura_set.exists():
        # Si ya existe una factura, actualizamos los estados
        factura = reserva.factura_set.first()  # Obtener la primera factura
        messages.info(request, 'Esta reserva ya tiene una factura asociada. Los estados serán actualizados.')
    else:
        # Si no tiene factura, crear una nueva factura
        total = reserva.precio_total
        factura = Factura.objects.create(
            cliente=cliente,
            reserva=reserva,
            total=total,
            fecha_emision=timezone.now(),
            metodo_pago='Efectivo'  # O define otro valor predeterminado
        )
        messages.success(request, 'Factura generada exitosamente.')

    return redirect('adm_lista_facturas')

@login_required
@administrador_required
def modificar_factura(request, factura_id):
    # Obtener la factura por su ID
    factura = get_object_or_404(Factura, id=factura_id)

    if request.method == 'POST':
        # Obtener los datos del formulario
        fecha_emision = request.POST.get('fecha_emision')
        metodo_pago = request.POST.get('metodo_pago')
        total = request.POST.get('total')

        # Actualizar los campos de la factura
        factura.fecha_emision = fecha_emision
        factura.metodo_pago = metodo_pago
        factura.total = total

        # Guardar los cambios en la base de datos
        factura.save()

        # Redirigir a la página de detalle de la factura
        return redirect('adm_detalle_factura', factura_id=factura.id)

    # Renderizar el formulario con los datos actuales de la factura
    return render(request, 'factura/adm_modificar_factura.html', {'factura': factura})

@login_required
@administrador_required
def eliminar_factura(request, factura_id):
    # Obtener la factura correspondiente o devolver 404 si no existe
    factura = get_object_or_404(Factura, id=factura_id)
 # Obtener la reserva asociada antes de eliminar la factura
    reserva = factura.reserva
    auto = reserva.auto
    cliente = reserva.cliente

    # Eliminar la factura
    factura.delete()

    # Actualizar estados a como estaban antes de la factura
    reserva.estado_reserva = 'activa'
    auto.cambiar_estado('reservado')
    cliente.cambiar_estado('con_reserva')

    # Guardar los cambios
    reserva.save()
    auto.save()
    cliente.save()

    messages.success(request, 'Factura eliminada y estados actualizados correctamente.')
   
    return redirect('adm_lista_facturas')  # Asegúrate de que esta URL esté configurada





# Vistas para Trabajadores
@login_required
@administrador_required
def lista_trabajadores(request):
    trabajadores = get_user_model().objects.filter(is_staff=True)
    return render(request, 'trabajador/adm_lista_trabajadores.html', {'trabajadores': trabajadores})

@login_required
@administrador_required
def detalle_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(get_user_model(), id=trabajador_id)
    return render(request, 'trabajador/adm_detalle_trabajador.html', {'trabajador': trabajador})

@login_required
@administrador_required
def ingresar_trabajador(request):
    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            trabajador = form.save(commit=False)
            trabajador.is_staff = True
            trabajador.set_password(form.cleaned_data['password'])
            trabajador.save()
            return redirect('adm_lista_trabajadores')
    else:
        form = TrabajadorForm()
    return render(request, 'trabajador/adm_ingresar_trabajador.html', {'form': form})

@login_required
@administrador_required
def modificar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(get_user_model(), id=trabajador_id)
    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            if form.cleaned_data['password']:
                trabajador.set_password(form.cleaned_data['password'])
            form.save()
            return redirect('adm_lista_trabajadores')
    else:
        form = TrabajadorForm(instance=trabajador)
    return render(request, 'trabajador/adm_modificar_trabajador.html', {'form': form})

@login_required
@administrador_required
def eliminar_trabajador(request, trabajador_id):
    trabajador = get_object_or_404(get_user_model(), id=trabajador_id)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('adm_lista_trabajadores')
    return render(request, 'trabajador/adm_eliminar_trabajador.html', {'trabajador': trabajador})



@login_required
@administrador_required
def ingresar_politica(request):
    if request.method == 'POST':
        form = PoliticaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Política ingresada exitosamente.")
            return redirect('adm_lista_politicas')  # Redirige a la lista de políticas
        else:
            messages.error(request, "Hubo un error al ingresar la política. Verifique los datos.")
    else:
        form = PoliticaForm()
    return render(request, 'politicas/ingresar_politica.html', {'form': form})

def lista_politicas(request):
    # Obtener todas las políticas ingresadas por el administrador
    politicas = Politica.objects.all()

    return render(request, 'politicas/lista_politicas.html', {'politicas': politicas})

@login_required
@administrador_required
def modificar_politica(request, politica_id):
    politica = get_object_or_404(Politica, id=politica_id)
    if request.method == 'POST':
        form = PoliticaForm(request.POST, instance=politica)
        if form.is_valid():
            form.save()
            return redirect('adm_lista_politicas')
    else:
        form = PoliticaForm(instance=politica)
    return render(request, 'politicas/modificar_politica.html', {'form': form})

# Vista para Nosotros
@login_required
@administrador_required
def modificar_nosotros(request):

    nosotros = Nosotros.objects.first()
    if request.method == 'POST':
        form = NosotrosForm(request.POST, instance=nosotros)
        if form.is_valid():
            form.save()
            return redirect('adm_index')
    else:
        form = NosotrosForm(instance=nosotros)
    return render(request, 'nosotros/modificar_nosotros.html', {'form': form})



@login_required  
def generar_pdf(request, codigo_factura):  
    from reportlab.lib import colors  
    from reportlab.lib.pagesizes import letter  
    from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer  
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle  
    from reportlab.lib.units import inch  

    factura = get_object_or_404(Factura, codigo_factura=codigo_factura)  
    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = f'attachment; filename="boleta_{factura.codigo_factura}.pdf"'  

    doc = SimpleDocTemplate(response, pagesize=letter)  
    elements = []  
    styles = getSampleStyleSheet()  

    # Encabezado de la boleta  
    elements.append(Paragraph("BOLETA ELECTRÓNICA", styles['Title']))  
    elements.append(Spacer(1, 20))  

    # Información de la empresa  
    elements.append(Paragraph("RENT A CAR CHILE", styles['Heading1']))  
    elements.append(Paragraph("RUT: 26.546.705-0", styles['Normal']))  
    elements.append(Paragraph("Dirección: Calle Limache 3730, Viña del Mar", styles['Normal']))  
    elements.append(Paragraph("Teléfono: +56 9 7856 1034", styles['Normal']))  
    elements.append(Paragraph("Email: rentacarmarino06@gmail.com", styles['Normal']))  
    elements.append(Spacer(1, 20))  

    # Información de la boleta  
    elements.append(Paragraph(f"Boleta N°: {factura.codigo_factura}", styles['Heading2']))  
    elements.append(Paragraph(f"Fecha: {factura.fecha_emision.strftime('%d/%m/%Y')}", styles['Normal']))  
    elements.append(Spacer(1, 20))  

    # Información del cliente  
    elements.append(Paragraph("DATOS DEL CLIENTE", styles['Heading2']))  
    elements.append(Paragraph(f"Nombre: {factura.cliente.nombre} {factura.cliente.apellido}", styles['Normal']))  
    elements.append(Paragraph(f"RUT: {factura.cliente.rut}", styles['Normal']))  
    elements.append(Paragraph(f"Dirección: {factura.cliente.direccion}", styles['Normal']))  
    elements.append(Spacer(1, 20))  

    # Detalles del servicio  
    data = [  
        ['Descripción', 'Cantidad', 'Precio Unitario', 'Total'],  
        [f'Arriendo vehículo {factura.reserva.auto.marca} {factura.reserva.auto.modelo}',   
        f'{(factura.reserva.fecha_retorno - factura.reserva.fecha_inicio).days} días',  
        f'${factura.reserva.auto.precio_dia}',  
        f'${factura.total}'],  
        ['Seguro básico', '1', '\$10.000', '\$10.000'],  
    ]  

    table = Table(data, colWidths=[4*inch, 1*inch, 1.5*inch, 1*inch])  
    table.setStyle(TableStyle([  
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),  
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),  
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  
        ('FONTSIZE', (0, 0), (-1, 0), 14),  
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),  
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),  
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),  
        ('FONTSIZE', (0, 1), (-1, -1), 12),  
        ('GRID', (0, 0), (-1, -1), 1, colors.black)  
    ]))  

    elements.append(table)  
    elements.append(Spacer(1, 20))  

    # Totales  
    elements.append(Paragraph(f"Subtotal: ${factura.total}", styles['Normal']))  
    elements.append(Paragraph(f"IVA (19%): ${float(factura.total) * 0.19:.2f}", styles['Normal']))  
    elements.append(Paragraph(f"Total: ${float(factura.total) * 1.19:.2f}", styles['Normal']))  
    elements.append(Spacer(1, 30))  

    # Políticas y condiciones  
    elements.append(Paragraph("POLÍTICAS Y CONDICIONES", styles['Heading2']))  
    politicas = Politica.objects.all()  
    for politica in politicas:  
        elements.append(Paragraph(f"• {politica.titulo}: {politica.descripcion}", styles['Normal']))  

    # Seguro básico  
    elements.append(Spacer(1, 20))  
    elements.append(Paragraph("SEGURO BÁSICO INCLUIDO", styles['Heading2']))  
    elements.append(Paragraph("""  
    El seguro básico incluye:  
    - Cobertura por daños a terceros  
    - Asistencia en ruta 24/7  
    - Cobertura por robo  
    - Deducible: UF 10  
    """, styles['Normal']))  

    # Firmas  
    elements.append(Spacer(1, 40))  
    firma_data = [  
        ['_'*30, '_'*30],  
        ['Firma Cliente', 'Firma Empresa'],  
        [f'RUT: {factura.cliente.rut}', 'RUT: XX.XXX.XXX-X']  
    ]  
    firma_table = Table(firma_data, colWidths=[3*inch, 3*inch])  
    firma_table.setStyle(TableStyle([  
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  
    ]))  
    elements.append(firma_table)  

    # Generar PDF  
    doc.build(elements)  
    return response  




# views.py  
@login_required  
def descargar_politicas(request):  
    from reportlab.lib.pagesizes import letter  
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer  
    from reportlab.lib.styles import getSampleStyleSheet  

    response = HttpResponse(content_type='application/pdf')  
    response['Content-Disposition'] = 'attachment; filename="politicas_arriendo.pdf"'  

    doc = SimpleDocTemplate(response, pagesize=letter)  
    elements = []  
    styles = getSampleStyleSheet()  

    # Título  
    elements.append(Paragraph("POLÍTICAS DE ARRIENDO", styles['Title']))  
    elements.append(Spacer(1, 20))  

    # Obtener todas las políticas  
    politicas = Politica.objects.all()  
    for politica in politicas:  
        elements.append(Paragraph(politica.titulo, styles['Heading2']))  
        elements.append(Paragraph(politica.descripcion, styles['Normal']))  
        elements.append(Spacer(1, 10))  

    doc.build(elements)  
    return response  

@login_required  
@administrador_required  
def generar_reporte_autos(request):  
    autos = Auto.objects.all().values('patente', 'marca', 'modelo', 'estado_auto', 'combustible', 'año')  
    df_autos = pd.DataFrame(autos)  

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    response['Content-Disposition'] = 'attachment; filename=reporte_autos.xlsx'  

    with pd.ExcelWriter(response, engine='openpyxl') as writer:  
        df_autos.to_excel(writer, sheet_name='Autos', index=False)  

    return response  

@login_required  
@administrador_required  
def generar_reporte_reservas(request):  
    reservas = Reserva.objects.all().values('codigo_reserva', 'cliente__rut', 'auto__patente', 'fecha_inicio', 'fecha_retorno', 'estado_reserva', 'precio_total')  
    df_reservas = pd.DataFrame(reservas)  

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    response['Content-Disposition'] = 'attachment; filename=reporte_reservas.xlsx'  

    with pd.ExcelWriter(response, engine='openpyxl') as writer:  
        df_reservas.to_excel(writer, sheet_name='Reservas', index=False)  

    return response  

@login_required  
@administrador_required  
def generar_reporte_clientes(request):  
    clientes = Cliente.objects.all().values('rut', 'nombre', 'apellido', 'estado_cliente')  
    df_clientes = pd.DataFrame(clientes)  

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    response['Content-Disposition'] = 'attachment; filename=reporte_clientes.xlsx'  

    with pd.ExcelWriter(response, engine='openpyxl') as writer:  
        df_clientes.to_excel(writer, sheet_name='Clientes', index=False)  

    return response  

@login_required  
@administrador_required  
def generar_reporte_facturas(request):  
    facturas = Factura.objects.all().values('codigo_factura', 'reserva__codigo_reserva', 'cliente__rut', 'fecha_emision', 'metodo_pago', 'total')  
    df_facturas = pd.DataFrame(facturas)  

    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')  
    response['Content-Disposition'] = 'attachment; filename=reporte_facturas.xlsx'  

    with pd.ExcelWriter(response, engine='openpyxl') as writer:  
        df_facturas.to_excel(writer, sheet_name='Facturas', index=False)  

    return response

def reservas_vencidas(request):
    """
    Vista que lista todas las reservas vencidas (fecha de retorno pasada)
    para mostrarlas en la interfaz.
    """
    reservas_vencidas = Reserva.objects.filter(fecha_retorno__lt=now().date(), estado_reserva__in=['activa', 'pagada'])
    return render(request, 'reserva/adm_reservas_vencidas.html', {'reservas_vencidas': reservas_vencidas or []})