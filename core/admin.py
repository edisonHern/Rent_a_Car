from django.contrib import admin
from core.models import CustomUser

class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff', 'is_active')  # Campos visibles en la lista
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')  # Filtros en la barra lateral
    search_fields = ('username', 'email')  # Campos para buscar
    ordering = ('username',)  # Ordenar por nombre de usuario

    # Filtrar usuarios para mostrar solo administradores y trabajadores
    def get_queryset(self, request):
        queryset = super().get_queryset(request)
        return queryset.filter(tipo_usuario__in=['administrador', 'trabajador'])

# Registrar el modelo con la configuración personalizada
admin.site.register(CustomUser, CustomUserAdmin)



from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

class CustomAdminSite(admin.AdminSite):
    def has_permission(self, request):
        return request.user.is_authenticated and request.user.tipo_usuario == 'administrador'

admin_site = CustomAdminSite(name='custom_admin')