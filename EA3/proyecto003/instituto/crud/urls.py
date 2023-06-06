from . import views
from django.urls import path

urlpatterns = [
    path('marca', views.marca, name='marca'),
    path('categoria', views.categoria, name='categoria'),
    path('genero', views.genero, name='genero'),
    path('clienteForm', views.clienteForm, name='clienteForm'),
    path('menu', views.menu, name='menu'),
]

# 127.0.0.1:8000/crud/marca
# 
# EJERCICIOS: crear crud categoria y genero
# TAREA 2: crear modelo para producto
# tarea 3: al logout preguntar al usuario si está seguro de cerrar sesión