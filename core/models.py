#models.py
from django.db import models
from django.utils import timezone
import random
import string
from django.core.exceptions import ValidationError
from django.contrib.auth.models import AbstractUser
import uuid  # Para generar códigos aleatorios
from django.shortcuts import get_object_or_404, render
from django.core.validators import RegexValidator
from django.conf import settings



class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Aseguramos que el correo sea único

    # Agrega el campo tipo_usuario si es necesario
    TIPO_USUARIO_CHOICES = [
        ('cliente', 'Cliente'),
        ('trabajador', 'Trabajador'),
        ('administrador', 'Administrador'),
    ]
    tipo_usuario = models.CharField(
        max_length=20,
        choices=TIPO_USUARIO_CHOICES,
        default='cliente',  # Valor predeterminado
    )

    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.username




class Auto(models.Model):
    ESTADO_CHOICES = [
        ('disponible', 'Disponible'),
        ('reservado', 'Reservado'),  # Incluye 'reservado' si es necesario
        ('rentado', 'Rentado'),
        ('mantenimiento', 'Mantenimiento'),
        ('no_disponible', 'No Disponible'),
        
    ]

    MARCA_CHOICES = [
        ('gasolina', 'Gasolina'),
        ('diesel', 'Diesel'),
        ('electrico', 'Electrico')
    ]
    
    marca = models.CharField(max_length=100, null=False, blank=False)
    modelo = models.CharField(max_length=100, null=False, blank=False)
    año = models.PositiveIntegerField()
    patente = models.CharField(max_length=10, unique=True)
    color = models.CharField(max_length=50, blank=True, null=True) 
    puertas = models.PositiveIntegerField()
    precio_dia = models.PositiveIntegerField(null=False,blank=False)
    kilometraje = models.PositiveIntegerField(null=False, blank=False)
    estado_auto = models.CharField(
        max_length=20,
        choices=ESTADO_CHOICES,  # Usamos la constante ESTADO_CHOICES aquí
        default='disponible'
    )

    combustible = models.CharField(
        max_length=50,
        choices=MARCA_CHOICES,  # Utilizamos las opciones definidas arriba
        default='Gasolina'  # Valor por defecto si no se selecciona nada
    )
    imagen = models.ImageField(upload_to='autos_imagenes/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.año})"
    
   
    

    def cambiar_estado(self, nuevo_estado):
        """Método para cambiar el estado del auto."""
        if nuevo_estado not in dict(self.ESTADO_CHOICES):
            raise ValueError("Estado inválido para el auto.")
        self.estado_auto = nuevo_estado
        self.save()



def validar_rut(rut):
    """
    Valida un RUT chileno en formato XX.XXX.XXX-Y o X.XXX.XXX-Y.
    """
    # Eliminar puntos y guiones
    rut = rut.replace('.', '').replace('-', '')

    # Verificar que el RUT tenga al menos 8 caracteres (7 del cuerpo + 1 del dígito verificador)
    if len(rut) < 8:
        return False

    # Separar el cuerpo y el dígito verificador
    cuerpo = rut[:-1]
    dv = rut[-1].upper()

    # Validar que el cuerpo sea numérico
    if not cuerpo.isdigit():
        return False

    # Calcular el dígito verificador
    suma = 0
    multiplicador = 2

    for i in range(len(cuerpo) - 1, -1, -1):
        suma += int(cuerpo[i]) * multiplicador
        multiplicador = multiplicador + 1 if multiplicador < 7 else 2

    dv_calculado = 11 - (suma % 11)
    if dv_calculado == 11:
        dv_calculado = '0'
    elif dv_calculado == 10:
        dv_calculado = 'K'
    else:
        dv_calculado = str(dv_calculado)

    # Comparar el dígito verificador calculado con el proporcionado
    return dv == dv_calculado

# Lista de regiones de Chile
REGIONES = [
    ('V', 'Región de Valparaíso'),
    ('RM', 'Región Metropolitana'),
    ('I', 'Región de Tarapacá'),
    ('II', 'Región de Antofagasta'),
    ('III', 'Región de Atacama'),
    ('IV', 'Región de Coquimbo'),
    ('VI', 'Región del Libertador General Bernardo O’Higgins'),
    ('VII', 'Región del Maule'),
    ('VIII', 'Región del Biobío'),
    ('IX', 'Región de La Araucanía'),
    ('X', 'Región de Los Lagos'),
    ('XI', 'Región de Aysén del General Carlos Ibáñez del Campo'),
    ('XII', 'Región de Magallanes y de la Antártica Chilena'),
    ('XIV', 'Región de Los Ríos'),
    ('XV', 'Región de Arica y Parinacota'),
    ('XVI', 'Región de Ñuble'),
]


class Cliente(models.Model):
    ESTADOS_CLIENTE = [
        ('inactivo', 'Inactivo'),
        ('con_reserva', 'Con Reserva'),
        ('rentando', 'Rentando'),
    ]

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,   # Reference to the CustomUser model
        on_delete=models.CASCADE,
        related_name='cliente', # Optional: allows reverse access (e.g., user.cliente)
        null=True,  # Allow null values if some clients are not linked to users
        blank=True
    )
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    rut = models.CharField(max_length=12, 
                        unique=True, 
                        validators=[validar_rut],  # Aplica la validación personalizada
                        )  # Número único de identificación
    fecha_nac = models.DateField(null=True, blank=True, verbose_name="Fecha nacimiento")  # Nueva columna para fecha de nacimiento
    region = models.CharField(max_length=50, choices=REGIONES, default='Región de Valparaiso')
    ciudad = models.CharField(max_length=50, blank=False, null=False)
    licencia_conducir = models.CharField(max_length=20, blank=False, null=False,
                                    validators=[
            RegexValidator(
                regex=r'^[A-Za-z]-[A-Za-z0-9]{5}-[A-Za-z0-9]{3}$',  # Valida el formato X-XXXXX-XXX
                message="La licencia debe seguir el formato X-XXXXX-XXX, por ejemplo: B-K23YT-6H8")])

    telefono = models.CharField(max_length=15, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False, null=False)
    direccion = models.CharField(max_length=100, blank=False, null=False)
    estado_cliente = models.CharField(max_length=12, choices=ESTADOS_CLIENTE, default='inactivo')
    imagen = models.ImageField(upload_to='clientes_imagenes/', blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.rut})"
    

#Verifica cambios de estados del cliente
    def cambiar_estado(self, nuevo_estado):
        """Método genérico para cambiar el estado del cliente."""
        if nuevo_estado not in dict(self.ESTADOS_CLIENTE):
                raise ValueError("Estado inválido para el cliente")
        self.estado_cliente = nuevo_estado
        self.save()




from django.utils import timezone
from django.db import models
from django.core.exceptions import ValidationError
import random
import string


class Reserva(models.Model):
    codigo_reserva = models.CharField(max_length=10, unique=True, editable=False)
    auto = models.ForeignKey(Auto, on_delete=models.CASCADE, related_name='reservas')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='reservas')
    fecha_reserva = models.DateTimeField(default=timezone.now)
    fecha_inicio = models.DateField(null=False, blank=False)  # Fecha de inicio de la reserva
    fecha_retorno = models.DateField(null=False, blank=False)  # Fecha de retorno esperada
    precio_total = models.PositiveIntegerField(null=True,blank=True)
    estado_reserva = models.CharField(
        max_length=20,
        choices=[('activa', 'Activa'), ('completada', 'Completada'), ('cancelada', 'Cancelada'),('pagada', 'Pagada')],
        default='activa'
    )

    def __str__(self):
        return f"Reserva {self.codigo_reserva} de {self.auto} por {self.cliente}"
    

#Genera codigos random para reservas
    def generar_codigo_unico(self):
        while True:
        # Genera un código con solo números (10 dígitos)
            codigo = ''.join(random.choices(string.digits, k=10))
            if not Reserva.objects.filter(codigo_reserva=codigo).exists():
                return codigo
            

#No deja que se dupliquen las reservas con mismos autos y fechas
    def save(self, *args, **kwargs):
        # Solo hacemos la verificación si la reserva ya existe (modificación) y si se intentan cambiar las fechas.
        if self.pk:  # Si `self.pk` tiene un valor, significa que la reserva ya está en la base de datos.
            if self._has_changed('fecha_inicio') or self._has_changed('fecha_retorno'):
                # Verificamos si existe alguna otra reserva con el mismo auto y fechas conflictivas
                reserva_existente = Reserva.objects.filter(
                    auto=self.auto,
                    fecha_inicio=self.fecha_inicio,
                    fecha_retorno=self.fecha_retorno
                ).exclude(pk=self.pk)  # Excluir esta reserva de la búsqueda

                if reserva_existente.exists():
                    raise ValidationError("Este auto ya está reservado en las fechas seleccionadas.")

        # Generar el código de reserva solo si no existe
        if not self.codigo_reserva:
            self.codigo_reserva = self.generar_codigo_unico()

        # Guardar finalmente la instancia si no hay conflicto
            
        super().save(*args, **kwargs)


    def verificar_estado_reserva(self):
            """Verifica y actualiza los estados de la reserva y sus relaciones."""
            fecha_actual = timezone.now().date()
            # Logs de diagnóstico
            print(f"Verificando reserva {self.id}")
            print(f"Fecha actual: {fecha_actual}")
            print(f"Fecha retorno: {self.fecha_retorno}")
            print(f"Estado actual: {self.estado_reserva}")

            # BLOQUE 1: Verificación de fecha vencida
            # Si la fecha de retorno ya pasó, la reserva se marca como completada
            # independientemente de si tiene factura o no
            if fecha_actual > self.fecha_retorno and self.estado_reserva in ['activa', 'pagada']:
                print("La fecha de retorno ha pasado, cambiando a completada")
                self.estado_reserva = 'completada'
                self.auto.cambiar_estado('disponible')
                self.cliente.cambiar_estado('inactivo')
                self.save()
                self.auto.save()
                self.cliente.save()
                return

            # BLOQUE 2: Verificación de factura con fecha vigente
            # Si tiene factura y la fecha no ha pasado, mantiene estados de renta activa
            if self.factura_set.exists() and fecha_actual <= self.fecha_retorno:
                print(f"Reserva {self.id} tiene factura asociada y fecha vigente")
                self.estado_reserva = 'pagada'
                self.auto.cambiar_estado('rentado')
                self.cliente.cambiar_estado('rentando')
                self.save()
                self.auto.save()
                self.cliente.save()
                return

            # BLOQUE 3: Reserva activa con fecha futura
            # Si la fecha no ha pasado y la reserva está activa, mantiene estados de reserva
            if fecha_actual <= self.fecha_retorno and self.estado_reserva == 'activa':
                self.auto.cambiar_estado('reservado')
                self.cliente.cambiar_estado('con_reserva')
                self.auto.save()
                self.cliente.save()



            if self.estado_reserva == 'cancelada':
                self.auto.cambiar_estado('disponible')
                self.cliente.cambiar_estado('inactivo')
                self.save()

                self.auto.save()
                self.cliente.save()
                return


    
#Verifica conflicto de fechas    
    def _has_changed(self, field_name):
        """Verifica si el valor de un campo específico ha cambiado."""
        if not self.pk:
            return False  # Si no hay `pk`, es una reserva nueva
        old_value = Reserva.objects.get(pk=self.pk)  # Recupera el valor anterior de la reserva
        return getattr(old_value, field_name) != getattr(self, field_name)


    # Nueva funcionalidad: Verificar si la reserva está vencida
    def esta_vencida(self):
        """
        Determina si la reserva ha pasado su fecha de retorno.
        """
        return timezone.now().date() > self.fecha_retorno




def generar_codigo_factura():
    return uuid.uuid4().hex[:10].upper()




class Factura(models.Model):
    codigo_factura = models.CharField(
        max_length=10,
        unique=True,
        default=generar_codigo_factura  # Aquí usamos la función
    )
    total = models.PositiveIntegerField(null=False,blank=False)
    fecha_emision = models.DateField()  # Cambiar a DateField
    metodo_pago = models.CharField(
        max_length=50,
        choices=[
            ('Tarjeta Crédito', 'Tarjeta Crédito'),
            ('Tarjeta Debito', 'Tarjeta Debito'),
            ('Transferencia Bancaria', 'Transferencia Bancaria'),
            ('Efectivo', 'Efectivo'),
            ('Otro', 'Otro'),
        ],
        default='Tarjeta Debito'
    )
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)  # Cambiar a ForeignKey
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)

    def __str__(self):
        return f"Factura {self.codigo_factura} - {self.cliente} - {self.total}"



class Trabajador(models.Model):
    nombre = models.CharField(max_length=100, null=False, blank=False)
    apellido = models.CharField(max_length=100, null=False, blank=False)
    rut = models.CharField(
        max_length=12,
        unique=True,
        help_text="Ingrese el RUT en formato XX.XXX.XXX-Y"
    )
    cargo = models.CharField(max_length=50, null=True, blank=True, help_text="Cargo del trabajador (opcional)")
    telefono = models.CharField(max_length=15, null=True, blank=True, help_text="Teléfono del trabajador (opcional)")
    email = models.EmailField(null=True, blank=True, help_text="Correo electrónico del trabajador (opcional)")

    def __str__(self):
        return f"{self.nombre} {self.apellido} - {self.rut}"





class Nosotros(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    mision = models.TextField()
    vision = models.TextField()
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo











class Politica(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()  # Agregar este campo
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    

# models.py  
class SeguroBasico(models.Model):  
    nombre = models.CharField(max_length=100, default="Seguro Básico")  
    descripcion = models.TextField()  
    precio = models.PositiveIntegerField(null=False,blank=False)
    deducible = models.CharField(max_length=50)  
    coberturas = models.TextField()  

    def __str__(self):  
        return self.nombre  
    
    