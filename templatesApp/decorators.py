# core/decorators.py
from django.http import HttpResponseForbidden

def trabajador_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.tipo_usuario == 'trabajador':
            return view_func(request, *args, **kwargs)
        return HttpResponseForbidden("No tienes permiso para acceder a esta página.")
    return _wrapped_view


