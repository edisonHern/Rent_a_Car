from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from core.models import Auto, Cliente, Reserva, Factura
from templatesApp.forms import AutoForm, ClienteForm, ReservaForm, FacturaForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.utils import timezone
from django.contrib.auth.forms import AuthenticationForm
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas



from templatesApp.decorators import trabajador_required
from django.shortcuts import render





def login_trabajador(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if user.tipo_usuario == 'trabajador'and user.is_staff:  # Verifica el rol
                login(request, user)
                return redirect('lista_autos')  # Redirige al dashboard del trabajador
            else:
                messages.error(request, "No tienes permisos de trabajador.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login/login_trabajador.html', {'form': form})


def logout_trabajador(request):
    logout(request)
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('carrusel_imagen')  # Redirige al login de trabajador




@login_required
@trabajador_required
def index(request):
    # Actualizar estados de autos y reservas antes de obtener las métricas
    reservas = Reserva.objects.all()
    for reserva in reservas:
        reserva.verificar_estado_reserva()

    autos = Auto.objects.all()
    for auto in autos:
        reservas_activas = Reserva.objects.filter(
            auto=auto,
            estado_reserva__in=['activa', 'pagada']
        ).exists()

        if reservas_activas and auto.estado_auto == 'disponible':
            auto.cambiar_estado('reservado')
            auto.save()

    # Obtener métricas de autos
    autos_disponibles = Auto.objects.filter(estado_auto='disponible').count()
    autos_reservados = Auto.objects.filter(estado_auto='reservado').count()
    autos_rentados = Auto.objects.filter(estado_auto='rentado').count()

    # Obtener métricas de clientes
    clientes_inactivos = Cliente.objects.filter(estado_cliente='inactivo').count()
    clientes_con_reserva = Cliente.objects.filter(estado_cliente='con_reserva').count()
    clientes_rentando = Cliente.objects.filter(estado_cliente='rentando').count()

    # Obtener métricas de reservas
    reservas_activas = Reserva.objects.filter(estado_reserva='activa').count()
    reservas_pagadas = Reserva.objects.filter(estado_reserva='pagada').count()
    reservas_completadas = Reserva.objects.filter(estado_reserva='completada').count()

    # Obtener total de facturas del mes actual
    from django.utils import timezone
    primer_dia_mes = timezone.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    facturas_mes = Factura.objects.filter(fecha_emision__gte=primer_dia_mes).count()

    context = {
        'autos': {
            'disponibles': autos_disponibles,
            'reservados': autos_reservados,
            'rentados': autos_rentados,
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
        },
        'facturas': {
            'total_mes': facturas_mes,
        }
    }

    return render(request, 'menu/index.html', context)

#Vistas para autos
@login_required
@trabajador_required
def lista_autos(request):
    query = request.GET.get('q')  # Término de búsqueda
    tipo_busqueda = request.GET.get('tipo_busqueda')  # Tipo de búsqueda seleccionado
    estado_auto = request.GET.get('estado')  # Filtro por estado

    autos = Auto.objects.all()

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
    return render(request, 'auto/lista_autos.html', {'autos': autos})

@login_required
@trabajador_required
def detalle_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    return render(request, 'auto/detalle_auto.html', {'auto': auto})

@login_required
@trabajador_required
def ingresar_auto(request):
    if request.method == 'POST':
        form = AutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutoForm()
    return render(request, 'auto/ingresar_auto.html', {'form': form})

@login_required
@trabajador_required
def modificar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        form = AutoForm(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return redirect('lista_autos')
    else:
        form = AutoForm(instance=auto)
    return render(request, 'auto/modificar_auto.html', {'form': form})

@login_required
@trabajador_required
def eliminar_auto(request, id):
    auto = get_object_or_404(Auto, id=id)
    if request.method == 'POST':
        auto.delete()
        return redirect('lista_autos')
    return render(request, 'auto/eliminar_auto.html', {'auto': auto})






#Vistas para clientes
@login_required
@trabajador_required
def lista_clientes(request):
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

    return render(request, 'cliente/lista_clientes.html', {'clientes': clientes})

@login_required
@trabajador_required
def detalle_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    return render(request, 'cliente/detalle_cliente.html', {'cliente': cliente})

@login_required
@trabajador_required
def ingresar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cliente = form.save()
            return redirect('detalle_cliente', cliente_id=cliente.id)
    else:
        form = ClienteForm()
    return render(request, 'cliente/ingresar_cliente.html', {'form': form})

@login_required
@trabajador_required
def modificar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_clientes')  
    else:
        form = ClienteForm(instance=cliente)
    
    return render(request, 'cliente/modificar_cliente.html', {'form': form})

@login_required
@trabajador_required
def eliminar_cliente(request, cliente_id):
    cliente = get_object_or_404(Cliente, id= cliente_id)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_clientes')
    return render(request, 'cliente/eliminar_cliente.html', {'cliente': cliente})







#ESTADOS MANEJADOS
@login_required
@trabajador_required
def lista_reservas(request):    
    query = request.GET.get('q')
    tipo_busqueda = request.GET.get('tipo_busqueda')
    estado_reserva = request.GET.get('estado')

    # Primero verificar estados de todas las reservas
    reservas = Reserva.objects.all()
    for reserva in reservas:
        reserva.verificar_estado_reserva()

    # Verificar estados de autos
    autos = Auto.objects.all()
    for auto in autos:
        reservas_activas = Reserva.objects.filter(
            auto=auto,
            estado_reserva__in=['activa', 'pagada']
        ).exists()

        if reservas_activas and auto.estado_auto == 'disponible':
            auto.cambiar_estado('reservado')
            auto.save()

    # Aplicar filtros de búsqueda
    if query:
        if tipo_busqueda == 'codigo_reserva':
            reservas = reservas.filter(codigo_reserva__icontains=query)
        elif tipo_busqueda == 'patente':
            reservas = reservas.filter(auto__patente__icontains=query)
        elif tipo_busqueda == 'rut':
            reservas = reservas.filter(cliente__rut__icontains=query)

    if estado_reserva:
        reservas = reservas.filter(estado_reserva=estado_reserva)

    return render(request, 'reserva/lista_reservas.html', {'reservas': reservas})


@login_required
@trabajador_required
def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'reserva/detalle_reserva.html', {'reserva': reserva})

#ESTADOS MANEJADOS
def ingresar_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            
            # Obtener el auto seleccionado en el formulario
            auto = form.cleaned_data['auto']
            if auto.estado_auto == 'mantenimiento':
                messages.error(request, 'Este auto está en mantenimiento y no puede ser reservado.')
                return render(request, 'reserva/ingresar_reserva.html', {'form': form})
            
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



            # Cambiar el estado del auto a 'reservado'
             #auto.cambiar_estado('reservado')
             #auto.save()

            # Cambiar el estado del cliente a 'con_reserva'
             #cliente = reserva.cliente
             #cliente.cambiar_estado('con_reserva')
            # cliente.save()

            messages.success(request, 'Reserva creada con éxito.')
            return redirect('lista_reservas')

        else:
            messages.error(request, 'Hubo un error al crear la reserva.')
    else:
        form = ReservaForm()

    return render(request, 'reserva/ingresar_reserva.html', {'form': form})


@login_required
@trabajador_required
def modificar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)  
        if form.is_valid():
            reserva = form.save()
            reserva.verificar_estado_reserva()


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

        

            return redirect('lista_reservas')  
    else:
        form = ReservaForm(instance=reserva)
    
    return render(request, 'reserva/modificar_reserva.html', {'form': form})

#ESTADOS MANEJADOS
@login_required
@trabajador_required
def eliminar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    try:
        # Obtener el auto y cliente de la reserva
        auto = reserva.auto
        cliente = reserva.cliente

        # Verificar si el auto tiene otras reservas activas
        otras_reservas_auto = Reserva.objects.filter(
            auto=auto,
            estado_reserva='activa'
        ).exclude(id=reserva_id).exists()

        # Solo cambiar el estado del auto si no tiene otras reservas activas
        if not otras_reservas_auto:
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

    return redirect('lista_reservas')



@login_required
@trabajador_required
def cancelar_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)

    if reserva.estado_reserva in ['activa', 'pagada']:
        reserva.estado_reserva = 'cancelada'
        reserva.verificar_estado_reserva()
        messages.success(request, 'La reserva ha sido cancelada exitosamente.')
    else:
        messages.error(request, 'No se puede cancelar una reserva que ya está completada o cancelada.')

    return redirect('lista_reservas')




#Vista para facturas
@login_required
@trabajador_required
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

    return render(request, 'factura/lista_facturas.html', {'facturas': facturas})

@login_required
@trabajador_required
def detalle_factura(request, factura_id):
    factura = get_object_or_404(Factura, id=factura_id)
    return render(request, 'factura/detalle_factura.html', {'factura': factura})

#ESTADOS MANEJADOS
@login_required
@trabajador_required
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
            return redirect('adm_lista_facturas')  # Corregido el nombre del redirect
        else:
            messages.error(request, 'Hubo un error al crear la factura. Verifique los datos ingresados.')
    else:
        form = FacturaForm()

    return render(request, 'factura/ingresar_factura.html', {'form': form})


@login_required
@trabajador_required
def generar_factura_desde_reserva(request, reserva_id):
    # Obtener la reserva desde la base de datos
    reserva = get_object_or_404(Reserva, id=reserva_id)
    cliente = reserva.cliente
    auto = reserva.auto

    # Verificar si la reserva ya tiene una factura asociada
    if reserva.factura_set.exists():
        messages.info(request, 'Esta reserva ya tiene una factura asociada.')
        return redirect('lista_facturas')

    # Si no tiene factura, crear una nueva factura
    total = reserva.precio_total
    factura = Factura.objects.create(
        cliente=cliente,
        reserva=reserva,
        total=total,
        fecha_emision=timezone.now(),
        metodo_pago='Efectivo'
    )

    # Actualizar estados
    reserva.estado_reserva = 'pagada'
    auto.cambiar_estado('rentado')
    cliente.cambiar_estado('rentando')

    # Guardar los cambios
    reserva.save()
    auto.save()
    cliente.save()

    messages.success(request, 'Factura generada exitosamente y estados actualizados.')
    return redirect('lista_facturas')

@login_required
@trabajador_required
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
        return redirect('detalle_factura', factura_id=factura.id)

    # Renderizar el formulario con los datos actuales de la factura
    return render(request, 'factura/modificar_factura.html', {'factura': factura})

#ESTADOS MANEJADOS
@login_required
@trabajador_required
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
    return redirect('lista_facturas')


@login_required
@trabajador_required
def generar_pdf(request, codigo_factura):
    factura = get_object_or_404(Factura, codigo_factura=codigo_factura)

    # Crear el archivo PDF en la respuesta
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="factura_{factura.codigo_factura}.pdf"'

    # Crear un objeto de PDF
    p = canvas.Canvas(response, pagesize=letter)
    p.drawString(100, 750, f'Factura: {factura.codigo_factura}')
    p.drawString(100, 730, f'Cliente: {factura.cliente.rut}')
    p.drawString(100, 710, f'Reserva: {factura.reserva.codigo_reserva}')
    p.drawString(100, 690, f'Fecha de Emisión: {factura.fecha_emision}')
    p.drawString(100, 670, f'Método de Pago: {factura.metodo_pago}')
    p.drawString(100, 650, f'Total: ${factura.total}')

    # Finalizar y devolver el PDF
    p.showPage()
    p.save()
    
    return response



