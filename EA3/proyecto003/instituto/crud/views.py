from django.shortcuts import render
from .models import Marca

# Create your views here.
def marca(request):
    marcas = Marca.objects.all() # select * from Marca
    context= {"marcas": marcas}
    return render(request, 'marca.html', context)