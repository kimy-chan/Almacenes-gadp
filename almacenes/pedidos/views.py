from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import   login_required
from .forms import Formualrio_pedido
from almacenes.productos.models import Productos
from django.db.models import Q
from almacenes.utils.paginador import paginador_general
from almacenes.usuarios.models import Usuario
from almacenes.persona.models import Persona

from .models import Pedido

def index(request):
    if (request.method == 'POST'):
        id_categoria = request.POST.get('categoria_id')
        if not id_categoria:
            return redirect('index')
        productos_categoria= Productos.objects.select_related('categoria').filter(categoria_id=id_categoria)
        productos_categoria= paginador_general(request,productos_categoria)
    else:
        productos_categoria= Productos.objects.select_related('categoria').all()
        productos_categoria= paginador_general(request, productos_categoria)
    context ={
            'data':productos_categoria,
         
                }
    return render(request, 'pedidos/index.html', context)
   


def buscador(request):
    data_buscador = request.GET.get('buscador','')
    producto  = Productos.objects.select_related('categoria').filter(Q(nombre__icontains=data_buscador) | Q(codigo__icontains=data_buscador) |  Q(marca__icontains=data_buscador))
    producto = paginador_general(request, producto)
    context={
        'data':producto
        
    }
    return  render(request, 'pedidos/index.html', context)


def realizar_pedido(request, id_producto):
    id_usuario= request.user.id
    id_producto= id_producto
    if request.method =='POST':
        formulario=  Formualrio_pedido(request.POST)
        if formulario.is_valid():
            usuario = get_object_or_404(Usuario, id=id_usuario)
            producto = get_object_or_404(Productos, id=id_producto)
            pedido = formulario.save(commit=False)
            pedido.usuario=usuario
            pedido.producto= producto
            pedido.save()
            return HttpResponse('pedido realizado')
            
        else:
            formulario=  Formualrio_pedido(request.POST)
    else:
        formulario=  Formualrio_pedido()
        
    context={
        'forms': formulario
    }
    return render(request , 'pedidos/realizar_pedido.html', context)

def listar_pedidos(request):
    listando_pedidos = Pedido.objects.select_related('usuario', 'producto').all().distinct('usuario')

    context={
        'data':listando_pedidos
    }
    return render(request, 'pedidos/listar_pedido.html', context)

def informacion_pedido(request, id_usuario):
    print(id_usuario)
    datos_pedidos = Pedido.objects.select_related('usuario', 'producto').filter(usuario_id=id_usuario)
    datos_pedidos[0].usuario.persona.nombre
    for x in datos_pedidos:
        print(x.descripcion)
    context={
        'data': datos_pedidos
    }
    return render(request, 'pedidos/informacion_pedidos.html', context)