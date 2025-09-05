#forms.py
from django import forms
from core.models import Auto, Cliente, Reserva, Factura
from django.core.exceptions import ValidationError
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm









from django.shortcuts import render, redirect
from django.contrib import messages

from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser

class RegistroTrabajadorForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.tipo_usuario = 'trabajador'  # Asignar el rol de trabajador
        if commit:
            user.save()
        return user













class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            'marca', 'modelo', 'año', 'patente', 'color', 'puertas', 
            'precio_dia', 'kilometraje', 'combustible',
        ]
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'apellido', 'rut', 'fecha_nac',
            'licencia_conducir', 'telefono', 'email', 'direccion', 'ciudad', 'region',
        ]
        widgets = {
        'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 11111111-1'}),
        'licencia_conducir': forms.TextInput(attrs={'placeholder': 'Ejemplo: B-K23YT-6H8'}),
        'telefono': forms.TextInput(attrs={'placeholder': 'Ejemplo: +56912345678'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Ejemplo: juan.perez@email.com'}),
        'direccion': forms.TextInput(attrs={'placeholder': 'Ejemplo: Siempre Viva 123'}),
        'ciudad': forms.TextInput(attrs={'placeholder': 'Ejemplo: Viña del Mar'}),
        'fecha_nac': forms.DateInput(attrs={'type': 'date'}),  # Selector de fecha
        }
        labels = {
            'fecha_nac': 'Fecha de nacimiento',  # Alias para el campo
        }


class ReservaForm(forms.ModelForm):
    auto = forms.ModelChoiceField(  
        queryset=Auto.objects.all(),  # Cambiado para mostrar todos los autos  
        empty_label="Seleccione un auto",  
    )  

    cliente = forms.ModelChoiceField(  
        queryset=Cliente.objects.all(),  # Cambiado para mostrar todos los clientes  
        empty_label="Seleccione un cliente",  
    )  

    class Meta:
        model = Reserva
        fields = [
            'auto', 'cliente', 'fecha_reserva', 'fecha_inicio', 
            'fecha_retorno', 'precio_total', 'estado_reserva',
        ]
        widgets = {
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
            'fecha_retorno': forms.DateInput(attrs={'type': 'date'}),
        }


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Excluir la opción "Pagada" del campo estado_reserva
        self.fields['estado_reserva'].choices = [
            choice for choice in self.fields['estado_reserva'].choices if choice[0] != 'pagada'
        ]

    #ESTA INSTANCIA MANTIENE LAS FECHAS INTACTAS
        if self.instance.pk:  
            if self.instance.fecha_reserva:  
                self.initial['fecha_reserva'] = self.instance.fecha_reserva.strftime('%Y-%m-%dT%H:%M')
            if self.instance.fecha_inicio:  
                self.initial['fecha_inicio'] = self.instance.fecha_inicio.strftime('%Y-%m-%d')  
            if self.instance.fecha_retorno:  
                self.initial['fecha_retorno'] = self.instance.fecha_retorno.strftime('%Y-%m-%d')
















class FacturaForm(forms.ModelForm):

    reserva = forms.ModelChoiceField(
        queryset=Reserva.objects.filter(estado_reserva='activa'),  # Filtrar las reservas pendientes
        label="Seleccionar Reserva"
    )

    class Meta:
        model = Factura
        fields = ['codigo_factura', 'total', 'fecha_emision', 'metodo_pago', 'reserva']
        widgets = {
            'codigo_factura': forms.TextInput(attrs={'readonly': 'readonly'}),  # Solo lectura
            'total': forms.NumberInput(attrs={'min': '0'}),  # Valor mínimo para total
            'fecha_emision': forms.DateInput(attrs={'type': 'date'}),
        }
