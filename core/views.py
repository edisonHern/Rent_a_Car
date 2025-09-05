from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test  


def menu(request):
    return render(request, 'menu.html')

def is_cliente(user):
    return user.role == 'cliente'

def is_trabajador(user):
    return user.role == 'trabajador'

@login_required
@user_passes_test(is_cliente)
def cliente_dashboard(request):
    # Lógica para el dashboard del cliente
    return render(request, 'cliente_dashboard.html')

@login_required
@user_passes_test(is_trabajador)
def trabajador_dashboard(request):
    # Lógica para el dashboard del trabajador
    return render(request, 'trabajador_dashboard.html')









    



