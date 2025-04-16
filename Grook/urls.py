from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('_reload_/', include('django_browser_reload.urls')),

    path('admin/', admin.site.urls),

    path('', include('core.urls')),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)