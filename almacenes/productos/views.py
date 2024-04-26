
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_categoria,Formulario_productos



from .models import Categoria, Productos

# Create your views here.

def crear_categoria(request):    
    if(request.method == 'POST'):
        formulario= Formulario_categoria(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(reverse('crear_categoria'))
        else:
            formulario= Formulario_categoria(request.POST)  
    
    else:
        formulario= Formulario_categoria()  
    categorias = Categoria.objects.all()
    context={
        'form':formulario,
        'categorias':categorias
    }
    return render(request, 'productos/categoria/formulario.crear.html', context)

def crear_producto(request):
  
    if(request.method=='POST'):
        formulario= Formulario_productos(request.POST)
        if(formulario.is_valid()):
            formulario.save()
        else:
            formulario= Formulario_productos(request.POST)
    else: 
        formulario= Formulario_productos()
    context={
        'form':formulario
    }
    return render(request, 'productos/formulario.productos.html', context)


def listado_productos(request, id_categoria):#lista todos los productos por categoria
    listar_productos_categoria= Productos.objects.select_related('categoria').filter(categoria_id=id_categoria)
    nombre_categoria = Categoria.objects.get(pk=id_categoria)
    context={
        'productos':listar_productos_categoria,
        'nombre_categoria':nombre_categoria
    }
    return render(request, 'productos/listar_productos.html', context)

def informacion_producto(request, id_producto):
    info_producto= Productos.objects.get(pk= id_producto)
    context={
        'producto':info_producto
    }
    return render(request, 'productos/informacion_producto.html', context)