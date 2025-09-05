from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import CustomUser

@receiver(post_save, sender=CustomUser)
def asignar_tipo_usuario(sender, instance, created, **kwargs):
    if created and instance.tipo_usuario == 'cliente':
        # Aquí puedes agregar lógica adicional si es necesario
        print(f"Usuario cliente creado: {instance.username}")