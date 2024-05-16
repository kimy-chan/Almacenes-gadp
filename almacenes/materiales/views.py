
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_categoria,Formulario_materiales
from django.http import JsonResponse


from .models import Categoria, Materiales

# Create your views here.

def crear_categoria(request):    
    if(request.method == 'POST'):
        formulario= Formulario_categoria(request.POST)
        if formulario.is_valid():
            formulario.save()
            return JsonResponse({'data':True})
        else:
            formulario= Formulario_categoria(request.POST)
            errors=  dict(formulario.errors.items())
            return JsonResponse({'errores':errors})
    else:
        formulario= Formulario_categoria()  
    categorias = Categoria.objects.all().order_by('-fecha_creacion')
    context={
        'form':formulario,
        'categorias':categorias
    }
    return render(request, 'materiales/categoria/formulario.crear.html', context)

def crear_material(request):
  
    if(request.method=='POST'):
        formulario= Formulario_materiales(request.POST)
        if(formulario.is_valid()):
            material= formulario.save()
            material.calcular_total_paquetes()
            material.calcular_precio_total()

        else:
            formulario= Formulario_materiales(request.POST)
    else: 
        formulario= Formulario_materiales()
    context={
        'form':formulario
    }
    return render(request, 'materiales/formulario.material.html', context)


def listado_material(request, id_categoria):#lista todos los material por categoria
    listar_productos_categoria= Materiales.objects.select_related('categoria').filter(categoria_id=id_categoria)
    nombre_categoria = Categoria.objects.get(pk=id_categoria)
    context={
        'data':listar_productos_categoria,
        'nombre_categoria':nombre_categoria
    }
    return render(request, 'materiales/listar_material.html', context)

def informacion_material(request, id_material):
    info_producto= Materiales.objects.get(pk= id_material)
    context={
        'material':info_producto
    }
    return render(request, 'materiales/informacion_material.html', context)