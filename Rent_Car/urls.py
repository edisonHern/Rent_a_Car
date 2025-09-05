from django.urls import path, include  
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import reverse
from django.conf import settings
from django.conf.urls.static import static
from clientesApp.views import carrusel_imagen



urlpatterns = [

    path('admin/', admin.site.urls),  # URL para el panel de administración
    path('', carrusel_imagen, name='home'),
    path('core/', include('core.urls')),
    path('templatesApp/', include('templatesApp.urls')),
    path('clientesApp/', include('clientesApp.urls')),
    path('administradorApp/', include('administradorApp.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

