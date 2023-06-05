from django.shortcuts import render
from .models import Marca, Categoria, Genero

# importar los forms
from .forms import ClienteForm
# Create your views here.
"""def marca(request):
    marcas = Marca.objects.all() # select * from Marca
    context= {"marcas": marcas}
    return render(request, 'marca.html', context)"""

def clienteForm(request):
    context = {}
    if request.method == "POST":
        if 'Grabar' in request.POST:
            form = ClienteForm(request.POST)
            if form.is_valid():
                form.save()
                context = {'exito' : 'Los datos fueron guardados', 'form': ClienteForm }
            else:
                context = {'error' : 'Los datos NO fueron guardados', 'form': ClienteForm }
    else:
        context = {'form': ClienteForm}
        
    return render(request, 'clienteForm.html', context)

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
                context = {'exito':'Datos guardados'}
            else: #update
                try:
                    item = Marca.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito':'Datos guardados'}
                except:
                    context = {'error':'Error en la solicitud de guardar'}
        elif 'Listar' in request.POST:
            listado = Marca.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Marca.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error':'Error en la búsqueda del id especificado'}
        elif 'Eliminar' in request.POST:
            if id == 0:
                context = {'error': 'falta id para eliminar'}
            else:
                try:
                    item = Marca.objects.get(pk = id)
                    item.delete() 
                    context = {'exito': 'eliminado con éxito'}   
                except:
                    context = {'error':'Error en la eliminación del id especificado'}        
                
    
    return render(request, 'marca.html', context)

def categoria(request):
    context = {}

    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        #print(id, nombre, activo)

        if 'Grabar' in request.POST:
            if id == 0: # insert
                Categoria.objects.create(nombre=nombre, activo=activo)
                context = {'exito':'Datos guardados'}
            else: #update
                try:
                    item = Categoria.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito':'Datos guardados'}
                except:
                    context = {'error':'Error en la solicitud de guardar'}
        elif 'Listar' in request.POST:
            listado = Categoria.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Categoria.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error':'Error en la búsqueda del id especificado'}
        elif 'Eliminar' in request.POST:
            if id == 0:
                context = {'error': 'falta id para eliminar'}
            else:
                try:
                    item = Categoria.objects.get(pk = id)
                    item.delete() 
                    context = {'exito': 'eliminado con éxito'}   
                except:
                    context = {'error':'Error en la eliminación del id especificado'}        
                
    
    return render(request, 'categoria.html', context)

def genero(request):
    context = {}

    if request.method == 'POST':
        id = int("0" + request.POST['id'])
        nombre = request.POST['nombre']
        activo = 'activo' in request.POST

        #print(id, nombre, activo)

        if 'Grabar' in request.POST:
            if id == 0: # insert
                Genero.objects.create(nombre=nombre, activo=activo)
                context = {'exito':'Datos guardados'}
            else: #update
                try:
                    item = Genero.objects.get(pk = id)
                    item.nombre = nombre
                    item.activo = activo
                    item.save()
                    context = {'exito':'Datos guardados'}
                except:
                    context = {'error':'Error en la solicitud de guardar'}
        elif 'Listar' in request.POST:
            listado = Genero.objects.all()
            context = {'listado': listado}
        elif 'Buscar' in request.POST:
            try:
                item = Genero.objects.get(pk = id)
                context = {'item': item}
            except:
                context = {'error':'Error en la búsqueda del id especificado'}
        elif 'Eliminar' in request.POST:
            if id == 0:
                context = {'error': 'falta id para eliminar'}
            else:
                try:
                    item = Genero.objects.get(pk = id)
                    item.delete() 
                    context = {'exito': 'eliminado con éxito'}   
                except:
                    context = {'error':'Error en la eliminación del id especificado'}        
                
    
    return render(request, 'genero.html', context)