from django.urls import path 
from templatesApp import views












urlpatterns = [
    
    path('index/', views.index, name='index'), 
    

    #urls para autos
    path('autos/', views.lista_autos, name='lista_autos'),
    path('autos/detalle/<int:auto_id>/', views.detalle_auto, name='detalle_auto'),
    #CRUD autos
    path('autos/ingresar/', views.ingresar_auto, name='ingresar_auto'),
    path('autos/modificar/<int:id>/', views.modificar_auto, name='modificar_auto'),
    path('autos/eliminar/<int:id>/', views.eliminar_auto, name='eliminar_auto'),

    #urls para clientes
    path('clientes/', views.lista_clientes, name='lista_clientes'),
    path('clientes/detalle/<int:cliente_id>/', views.detalle_cliente, name='detalle_cliente'),
    #CRUD clientes
    path('clientes/ingresar/', views.ingresar_cliente, name='ingresar_cliente'),
    path('cliente/modificar/<int:cliente_id>/', views.modificar_cliente, name='modificar_cliente'),
    path('cliente/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='eliminar_cliente'),

    #urls para reservas
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/detalle/<int:reserva_id>/', views.detalle_reserva, name='detalle_reserva'),
    #CRUD reservas
    path('reservas/agregar/', views.ingresar_reserva, name='ingresar_reserva'),
    path('reserva/actualizar/<int:reserva_id>/', views.modificar_reserva, name='modificar_reserva'),
    path('reserva/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='eliminar_reserva'),
    path('cancelar/reserva/<int:reserva_id>/', views.cancelar_reserva, name='cancelar_reserva'),

    #urls para facturas
    path('lista_facturas/', views.lista_facturas, name='lista_facturas'),
    path('ingresar_factura/', views.ingresar_factura, name='ingresar_factura'),
    #CRUD facturas
    path('reservas/<int:reserva_id>/generar_factura/', views.generar_factura_desde_reserva, name='generar_factura_desde_reserva'),
    path('factura/detalle/<str:factura_id>/', views.detalle_factura, name='detalle_factura'),
    path('factura/modificar/<str:factura_id>/', views.modificar_factura, name='modificar_factura'),
    path('factura/eliminar/<str:factura_id>/', views.eliminar_factura, name='eliminar_factura'),

    path('factura/generar_pdf/<str:codigo_factura>/', views.generar_pdf, name='generar_pdf'),

    path('login/trabajador/', views.login_trabajador, name='login_trabajador'),
    path('logout/trabajador/', views.logout_trabajador, name='logout_trabajador'),
]