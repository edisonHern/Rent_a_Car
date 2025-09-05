from django.http import HttpResponseForbidden
from django.shortcuts import redirect
from django.conf import settings

def administrador_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        # Verifica si el usuario está autenticado
        if not request.user.is_authenticated:
            # Redirige al LOGIN_URL si no está autenticado
            return redirect(settings.LOGIN_URL)

        # Verifica si el usuario es administrador
        if request.user.tipo_usuario == 'administrador':
            return view_func(request, *args, **kwargs)

        # Si no es administrador, devuelve un error 403
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")

    return _wrapped_view
