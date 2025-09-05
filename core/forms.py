# forms.py
from django import forms
from django.contrib import admin
from core.models import CustomUser
from django import forms
from .models import CustomUser











class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'tipo_usuario', 'is_staff', 'is_active']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Limitar las opciones de tipo_usuario a trabajador y administrador
        self.fields['tipo_usuario'].choices = [
            ('trabajador', 'Trabajador'),
            ('administrador', 'Administrador'),
        ]

class CustomUserAdmin(admin.ModelAdmin):
    form = CustomUserForm
    list_display = ('username', 'email', 'tipo_usuario', 'is_staff', 'is_active')
    list_filter = ('tipo_usuario', 'is_staff', 'is_active')
    search_fields = ('username', 'email')

admin.site.register(CustomUser, CustomUserAdmin)