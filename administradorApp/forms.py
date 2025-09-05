#forms.py
from django import forms
from core.models import Auto, Cliente, Reserva, Factura, Politica, Nosotros
from django.core.exceptions import ValidationError
from django.contrib import messages 
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from core.models import CustomUser
from core.models import Trabajador







class RegistroAdministradorForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo Electrónico")

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.tipo_usuario = 'administrador'  # Asignar el rol de administrador
        if commit:
            user.save()
        return user




class AutoForm(forms.ModelForm):
    class Meta:
        model = Auto
        fields = [
            'marca', 'modelo', 'año', 'patente', 'color', 'puertas', 
            'precio_dia', 'kilometraje', 'combustible',
            'estado_auto', 'imagen'
        ]
        widgets = {
            'marca': forms.TextInput(attrs={'placeholder': 'Ejemplo: Toyota'}),
            'modelo': forms.TextInput(attrs={'placeholder': 'Ejemplo: Yaris'}),
            'año': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 2021'}),
            'patente': forms.TextInput(attrs={'placeholder': 'Ejemplo: ABCD23'}),
            'color': forms.TextInput(attrs={'placeholder': 'Ejemplo: Rojo'}),
            'puertas': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 4'}),
            'precio_dia': forms.NumberInput(attrs={'placeholder': 'Ejemplo: $30.000'}),
            'kilometraje': forms.NumberInput(attrs={'placeholder': 'Ejemplo: 5000'}),
        }
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            'nombre', 'apellido', 'rut', 'fecha_nac',
            'licencia_conducir', 'telefono', 'email', 'direccion', 'ciudad', 'region'
        ]
        widgets = {
        'rut': forms.TextInput(attrs={'placeholder': 'Ejemplo: 11111111-1'}),
        'licencia_conducir': forms.TextInput(attrs={'placeholder': 'Ejemplo: B-K23YT-6H8'}),
        'telefono': forms.TextInput(attrs={'placeholder': 'Ejemplo: +56912345678'}),
        'email': forms.EmailInput(attrs={'placeholder': 'Ejemplo: juan.perez@email.com'}),
        'direccion': forms.TextInput(attrs={'placeholder': 'Ejemplo: Siempre Viva 123'}),
        'ciudad': forms.TextInput(attrs={'placeholder': 'Ejemplo: Viña del Mar'}),
        'fecha_nac': forms.DateInput(attrs={'type': 'date', 'readonly': False }),  # Selector de fecha
        }
        labels = {
            'fecha_nac': 'Fecha de nacimiento',  # Alias para el campo
        }

        def __init__(self, *args, **kwargs):  
            super().__init__(*args, **kwargs)  
            if self.instance and self.instance.fecha_nac:  
                self.initial['fecha_nac'] = self.instance.fecha_nac.strftime('%Y-%m-%d')


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
            'fecha_retorno', 'precio_total', 'estado_reserva'  
        ]  
        widgets = {  
            'fecha_reserva': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),  
            'fecha_retorno': forms.DateInput(attrs={'type': 'date'}),  
            'precio_total': forms.NumberInput(attrs={'placeholder': 'Ejemplo: \$30.000'}),  
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

        # Si es una instancia existente (modificación)  
        if self.instance and self.instance.pk:  
            # Establecer el queryset para mostrar solo el auto y cliente actual  
            self.fields['auto'].queryset = Auto.objects.filter(id=self.instance.auto.id)  
            self.fields['cliente'].queryset = Cliente.objects.filter(id=self.instance.cliente.id)  
            # Establecer los valores iniciales  
            self.fields['auto'].initial = self.instance.auto  
            self.fields['cliente'].initial = self.instance.cliente  

    


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






class TrabajadorForm(forms.ModelForm):
    class Meta:
        model = Trabajador
        fields = ['nombre', 'apellido', 'rut', 'cargo', 'telefono', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellido'}),
            'rut': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'RUT'}),
            'cargo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cargo'}),
            'telefono': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Teléfono'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo Electrónico'}),
        }



class NosotrosForm(forms.ModelForm):
    class Meta:
        model = Nosotros
        fields = ['titulo', 'contenido', 'mision', 'vision']




class PoliticaForm(forms.ModelForm):
    class Meta:
        model = Politica
        fields = ['titulo', 'descripcion']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Título de la política'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción de la política'}),
        }