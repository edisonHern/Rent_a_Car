from django.urls import path 
from administradorApp import views
from django.conf import settings  
from django.conf.urls.static import static
from .views import reservas_vencidas



urlpatterns = [
    
    path('adm_index/', views.adm_index, name='adm_index'), 
    #urls para autos
    path('adm/autos/', views.adm_lista_autos, name='adm_lista_autos'),
    path('adm/autos/<int:auto_id>/', views.detalle_auto, name='adm_detalle_auto'),
    #CRUD autos
    path('adm/autos/ingresar/', views.ingresar_auto, name='adm_ingresar_auto'),
    path('adm/autos/modificar/<int:id>/', views.modificar_auto, name='adm_modificar_auto'),
    path('adm/autos/eliminar/<int:id>/', views.eliminar_auto, name='adm_eliminar_auto'),

    #urls para clientes
    path('adm/clientes/', views.adm_lista_clientes, name='adm_lista_clientes'),
    path('adm/clientes//<int:cliente_id>/', views.detalle_cliente, name='adm_detalle_cliente'),
    #CRUD clientes
    path('adm/clientes/ingresar/', views.ingresar_cliente, name='adm_ingresar_cliente'),
    path('adm/cliente/modificar/<int:cliente_id>/', views.modificar_cliente, name='adm_modificar_cliente'),
    path('adm/cliente/eliminar/<int:cliente_id>/', views.eliminar_cliente, name='adm_eliminar_cliente'),

    #urls para reservas
    path('adm/reservas/', views.lista_reservas, name='adm_lista_reservas'),
    path('adm/reservas/detalles/<int:reserva_id>/', views.detalle_reserva, name='adm_detalle_reserva'),
    #CRUD reservas
    path('adm/reservas/agregar/', views.ingresar_reserva, name='adm_ingresar_reserva'),
    path('adm/reserva/actualizar/<int:reserva_id>/', views.modificar_reserva, name='adm_modificar_reserva'),
    path('adm/reserva/eliminar/<int:reserva_id>/', views.eliminar_reserva, name='adm_eliminar_reserva'),
    path('adm/cancelar/reserva/<int:reserva_id>/', views.cancelar_reserva, name='adm_cancelar_reserva'),

    #urls para facturas
    path('adm/lista_facturas/', views.lista_facturas, name='adm_lista_facturas'),
    path('adm/ingresar_factura/', views.ingresar_factura, name='adm_ingresar_factura'),
    #CRUD facturas
    path('adm/reservas/<int:reserva_id>/generar_factura/', views.generar_factura_desde_reserva, name='adm_generar_factura_desde_reserva'),
    path('adm/factura/detalle/<str:factura_id>/', views.detalle_factura, name='adm_detalle_factura'),
    path('adm/factura/modificar/<str:factura_id>/', views.modificar_factura, name='adm_modificar_factura'),
    path('adm/factura/eliminar/<str:factura_id>/', views.eliminar_factura, name='adm_eliminar_factura'),

    path('adm/factura/generar_pdf/<str:codigo_factura>/', views.generar_pdf, name='adm_generar_pdf'),
    path('descargar-politicas/', views.descargar_politicas, name='descargar_politicas'),  

    # Agregar estas URLs a urlpatterns
    path('adm/trabajadores/', views.lista_trabajadores, name='adm_lista_trabajadores'),
    path('adm/trabajadores/<int:trabajador_id>/', views.detalle_trabajador, name='adm_detalle_trabajador'),
    path('adm/trabajadores/ingresar/', views.ingresar_trabajador, name='adm_ingresar_trabajador'),
    path('adm/trabajadores/modificar/<int:trabajador_id>/', views.modificar_trabajador, name='adm_modificar_trabajador'),
    path('adm/trabajadores/eliminar/<int:trabajador_id>/', views.eliminar_trabajador, name='adm_eliminar_trabajador'),

    path('adm/lista/politicas/', views.lista_politicas, name='adm_lista_politicas'),
    path('adm/politicas/ingresar/', views.ingresar_politica, name='adm_ingresar_politica'),
    path('adm/politicas/modificar/<int:politica_id>/', views.modificar_politica, name='adm_modificar_politica'),

    path('reportes/autos/', views.generar_reporte_autos, name='reporte_autos'),  
    path('reportes/reservas/', views.generar_reporte_reservas, name='reporte_reservas'),  
    path('reportes/clientes/', views.generar_reporte_clientes, name='reporte_clientes'),  
    path('reportes/facturas/', views.generar_reporte_facturas, name='reporte_facturas'),

    path('adm/nosotros/modificar/', views.modificar_nosotros, name='adm_modificar_nosotros'),

    path('login/administrador/', views.login_administrador, name='login_administrador'),
    path('logout/administrador/', views.logout_administrador, name='logout_administrador'),

    path('reservas_vencidas/', reservas_vencidas, name='reservas_vencidas'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)