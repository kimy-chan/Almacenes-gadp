
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_categoria,Formulario_productos
from django.contrib.auth.decorators import login_required


from .models import Categoria

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
    formulario= Formulario_productos()
    context={
        'form':formulario
    }
    return render(request, 'productos/formulario.productos.html', context)