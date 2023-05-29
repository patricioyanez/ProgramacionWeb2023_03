from . import views
from django.urls import path

urlpatterns = [
    path('marca', views.marca, name='marca'),
]

# 127.0.0.1:8000/crud/marca