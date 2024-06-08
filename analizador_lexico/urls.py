# # user_chat/urls.py Rutas de la aplicación
from django.urls import path, re_path
from .views import index


urlpatterns = [
    path('', index, name='home'),
]