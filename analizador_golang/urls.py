# analizador_golang/urls.py Rutas de la aplicación
from django.urls import path, re_path
from .views import analyze_code


urlpatterns = [
    path('go/', analyze_code, name='home'),
]