from django.shortcuts import render
from .models import Marca

# Create your views here.
"""def marca(request):
    marcas = Marca.objects.all() # select * from Marca
    context= {"marcas": marcas}
    return render(request, 'marca.html', context)"""

def marca(request):
    context = {}

    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        #print(id, nombre, activo)

        if 'Grabar' in request.POST:
            if id == 0: # insert
                Marca.objects.create(nombre=nombre, activo=activo)
            else: #update
                item = Marca.objects.get(pk = id)
                item.nombre = nombre
                item.activo = activo
                item.save()
        elif 'Listar' in request.POST:
            listado = Marca.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            item = Marca.objects.get(pk = id)
            context = {'item': item}
        elif 'Eliminar' in request.POST:
            if id == 0:
                context = {'mensaje': 'falta id para eliminar'}
            else:
                item = Marca.objects.get(pk = id)
                item.delete() 
                context = {'mensaje': 'eliminado con éxito'}           
                
    
    return render(request, 'marca.html', context)