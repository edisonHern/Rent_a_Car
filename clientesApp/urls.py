from django.urls import path
from clientesApp import views


urlpatterns = [
    
    path('cl_reservas/', views.cl_ver_reservas, name='cl_ver_reservas'),
    path('cl_detalle_reserva/<int:reserva_id>/', views.cl_detalle_reserva, name='cl_detalle_reserva'),
    path('cl_crear_reserva/nueva/<int:cliente_id>/<int:auto_id>/', views.cl_crear_reserva, name='cl_crear_reserva'),
    path('cl_crear_cliente/nueva/', views.cl_crear_cliente, name='cl_crear_cliente'),


    path('catalogo/', views.catalogo, name='catalogo'),
    path('perfil/', views.perfil, name='perfil'),
    path('ver_politicas/', views.ver_politicas, name='ver_politicas'),
    path('nosotros/', views.nosotros, name='nosotros'),
    path('menu_cliente', views.menu_cliente, name='menu_cliente'),
    path('ver_detalles_autos/<int:auto_id>/,', views.ver_detalles_auto, name='ver_detalles_auto'),
    path('staff/', views.staff, name='staff'),



    # Otras rutas de clientesApp
    path('login/cliente/',views.login_cliente, name='login_cliente'),
    path('registro_cliente/', views.registro_cliente, name='registro_cliente'),
    path('logout/', views.logout_cliente, name='logout_cliente'),  # Define la ruta para logout

#carrusel

    path('', views.carrusel_imagen, name='carrusel_imagen'),

] 