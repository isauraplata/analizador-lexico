from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('analizador_lexico.urls')),
    path('', include('analizador2.urls')),
    path('', include('examen.urls')),
    path('', include('analizador_lexico_sinonimos.urls')),
    path('', include('analizador_golang.urls')),
    path('', include('analizador_semantico.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
