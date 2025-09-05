from django import forms
from core.models import Reserva, Auto, Cliente  # Importamos el modelo de core
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date




    

from django import forms
from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser

class RegistroClienteForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']  # Campos del formulario

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.tipo_usuario = 'cliente'
        if commit:
            user.save()
        return user





class ReservaForm(forms.ModelForm):
   

    class Meta:
        model = Reserva
        fields = ['fecha_inicio', 'fecha_retorno']
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_retorno': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
        labels = {
            'fecha_inicio': 'Fecha de Inicio',
            'fecha_retorno': 'Fecha de Retorno',
        }

    def clean(self):
        cleaned_data = super().clean()
        fecha_inicio = cleaned_data.get('fecha_inicio')
        fecha_retorno = cleaned_data.get('fecha_retorno')

        # Validar que la fecha de inicio sea anterior a la fecha de retorno
        if fecha_inicio and fecha_retorno and fecha_inicio > fecha_retorno:
            raise forms.ValidationError("La fecha de inicio no puede ser posterior a la fecha de retorno.")

        # Validar que la fecha de inicio no sea anterior a la fecha actual
        if fecha_inicio and fecha_inicio < date.today():
            raise forms.ValidationError("La fecha de inicio debe ser igual o posterior a la fecha actual.")
        return cleaned_data




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

    def clean_rut(self):
        rut = self.cleaned_data.get('rut')
        if not rut:
            raise forms.ValidationError("El campo RUT no puede estar vacío.")
        # Add additional validation logic for RUT if necessary
        return rut