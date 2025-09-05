from django.shortcuts import render, redirect, get_object_or_404
from .forms import ReservaForm
from core.models import Auto, Reserva, Cliente, Politica  
from templatesApp.forms import ClienteForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test 
from .forms import RegistroClienteForm
from django.conf import settings
import os
from django.core.paginator import Paginator






def catalogo(request):
    # Obtén todos los autos
    autos = Auto.objects.all()

    # Configura la paginación: 9 vehículos por página
    paginator = Paginator(autos, 9)  # 9 vehículos por página
    page_number = request.GET.get('page')  # Obtiene el número de página de la URL
    page_obj = paginator.get_page(page_number)  # Página actual

    # Renderiza el template con el contexto
    return render(request, 'catalogo.html', {'page_obj': page_obj})

"""def catalogo(request):
    # Obtener todos los autos disponibles
    autos = Auto.objects.all()  # O aplica filtros si solo quieres autos disponibles
    return render(request, 'catalogo.html', {'autos': autos})"""

def ver_detalles_auto(request, auto_id):
    auto = get_object_or_404(Auto, id=auto_id)
    cliente = None

    if request.user.is_authenticated:
        try:
            cliente = Cliente.objects.get(user=request.user)
        except Cliente.DoesNotExist:
            pass

    return render(request, 'ver_detalles_auto.html', {'auto': auto, 'cliente': cliente})

def cl_ver_reservas(request):    
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

    return render(request, 'ver_reservas.html', {'reservas': reservas})

def cl_detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    return render(request, 'detalle_reserva.html', {'reserva': reserva})



@login_required(login_url='login_cliente')  # Redirige a la URL 'login' si el usuario no está autenticado
def cl_crear_reserva(request, cliente_id, auto_id):
    # Obtener el cliente correspondiente al cliente_id
    
    cliente = get_object_or_404(Cliente, id=cliente_id, user=request.user)
    auto = get_object_or_404(Auto, id=auto_id)
        
    if auto_id:
        auto = get_object_or_404(Auto, id=auto_id)
    else:
        auto = None

    if request.method == 'POST':
        form = ReservaForm(request.POST)

        if form.is_valid():
            # Obtener el auto seleccionado en el formulario
            
            reserva_activa = Reserva.objects.filter(cliente=cliente, estado_reserva='activa').exists()
            if reserva_activa:
                messages.error(request, 'Ya tienes una reserva activa. No puedes crear otra.')
                return redirect('carrusel_imagen')  # Redirigir al menú del cliente

            # Verificar si el auto ya está reservado o rentado
            if auto.estado_auto in ['reservado', 'rentado']:
                messages.error(request, 'Este auto ya está reservado o rentado.')
                return render(request, 'crear_reserva.html', {'form': form, 'cliente': cliente, 'auto':auto})


            # Si el auto está disponible, crear la reserva
            reserva = form.save(commit=False)  # Crea la reserva sin guardarla en la base de datos
            reserva.cliente = cliente  # Asocia la reserva al cliente
            reserva.auto = auto
            reserva.estado_reserva = 'activa'  # Establecer el estado inicial de la reserva
            reserva.save()  # Guardar la reserva en la base de datos

            # Cambiar el estado del auto a 'reservado'
            auto.estado_auto = 'reservado'
            auto.save()
            cliente.estado_cliente = 'con_reserva'
            cliente.save()

            # Cambiar el estado del cliente (si es necesario)
            # Si no tienes un campo de estado en el modelo Cliente, puedes omitir esto
            # cliente.estado = 'con_reserva'
            # cliente.save()

            messages.success(request, 'Reserva creada con éxito.')

            # Redirigir a la lista de reservas
            return redirect('')

        else:
            # Si el formulario no es válido
            messages.error(request, 'Hubo un error al crear la reserva.')

    else:
        form = ReservaForm()

    # Renderizar el formulario con el cliente_id en el contexto
    return render(request, 'crear_reserva.html', {'form': form, 'cliente': cliente, 'auto': auto})


def is_cliente(user):
    return user.role == 'cliente'

@login_required(login_url='login_cliente')  # Redirige a la URL 'login' si el usuario no está autenticado
@user_passes_test(is_cliente)
def modificar_perfil_cliente(request):
    cliente = request.user.cliente
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado con éxito.')
            return redirect('perfil')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'modificar_perfil_cliente.html', {'form': form})

@login_required(login_url='login_cliente')  # Redirige a la URL 'login' si el usuario no está autenticado
def cl_crear_cliente(request):

        auto_id = request.GET.get('auto_id')
        try:
            cliente = Cliente.objects.get(user=request.user)
            print(f"Cliente encontrado: {cliente}")  # Depuración
            return redirect('cl_crear_reserva', cliente_id=cliente.id, auto_id=auto_id)  # Redirigir si el cliente ya existe
        except Cliente.DoesNotExist:
            print("Cliente no encontrado, procediendo al registro.")  # Depuración
            pass  # Si no existe, continúa con el registro

        if request.method == 'POST':
            form = ClienteForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                cliente = form.save(commit=False)
                cliente.user = request.user
                cliente = form.save()

                auto_id = request.GET.get('auto_id') or request.session.get('auto_id')
                if not auto_id:
                    messages.error(request, "No se encontró el ID del auto.")
                    return redirect('ver_detalles_auto')
                
                return redirect('cl_crear_reserva', cliente_id=cliente.id, auto_id=auto_id)
        else:
            form = ClienteForm()

            if auto_id:
                request.session['auto_id'] = auto_id

        return render(request, 'crear_cliente.html', {'form': form})




def menu_cliente(request):
    return render(request, 'carrusel_imagen.html')


@login_required(login_url='login_cliente')  # Redirige a la URL 'login' si el usuario no está autenticado
def perfil(request):
    # Obtener el cliente asociado al usuario actual
    try:  
        cliente = Cliente.objects.get(user=request.user)  
    except Cliente.DoesNotExist:  
        messages.warning(request, "Para acceder a tu perfil debes reservar un auto.")  
        return redirect('catalogo')  # Redirige a la página de registro de cliente

    reserva_activa = Reserva.objects.filter(cliente=cliente, estado_reserva='activa').first()

    context = {
        'cliente': cliente,
        'reserva_activa': reserva_activa,
    }

    return render(request, 'perfil.html', context)


def ver_politicas(request):
    # Obtener todas las políticas ingresadas por el administrador
    politicas = Politica.objects.all()

    return render(request, 'ver_politicas.html', {'politicas': politicas})


def nosotros(request):
    return render(request, 'nosotros.html')



def registro_cliente(request):
    if request.method == 'POST':
        form = RegistroClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "¡Registro exitoso! Ahora puedes iniciar sesión.")
            return redirect('login_cliente')  # Redirige al login después del registro
        else:
            messages.error(request, "Por favor, corrige los errores en el formulario.")
    else:
        form = RegistroClienteForm()
    return render(request, 'login/registro_cliente.html', {'form': form})

def login_cliente(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"¡Bienvenido, {user.username}!")
                return redirect('carrusel_imagen')  # Redirige a la página principal o donde desees
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    else:
        form = AuthenticationForm()
    return render(request, 'login/login_cliente.html', {'form': form})

def logout_cliente(request):

    logout(request)  # Cierra la sesión del usuario
    messages.success(request, "Has cerrado sesión correctamente.")
    return redirect('carrusel_imagen')  # Redirige a la vista 'menu'

def staff(request):

    """
    Vista para la página de Staff con dos botones:
    - Login Trabajador
    - Login Administrador
    """
    return render(request, 'login/staff.html')

def carrusel_imagen(request):
    # Ruta de la carpeta donde están las imágenes
    images_path = os.path.join(settings.MEDIA_ROOT, 'autos_imagenes')
    # Obtener nombres de las imágenes desde la carpeta
    images = [img for img in os.listdir(images_path) if img.endswith(('.jpg', '.png', '.jpeg'))]
    # Renderizar la plantilla con la lista de imágenes
    return render(request, 'carrusel_imagen.html', {'images': images})


