from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import   login_required
from .forms import Formualrio_pedido
from almacenes.materiales.models import Materiales
from django.db.models import Q
from almacenes.utils.paginador import paginador_general
from almacenes.usuarios.models import Usuario, Secretaria
from almacenes.persona.models import Persona
from datetime import datetime

from .models import Pedido

def index(request):
    if (request.method == 'POST'):
        id_categoria = request.POST.get('categoria_id')
        if not id_categoria:
            return redirect('index')
        productos_categoria= Materiales.objects.select_related('categoria').filter(categoria_id=id_categoria)
        productos_categoria= paginador_general(request,productos_categoria)
    else:
        productos_categoria= Materiales.objects.select_related('categoria').all()
        productos_categoria= paginador_general(request, productos_categoria)
    context ={
            'data':productos_categoria,
         
                }
    return render(request, 'pedidos/index.html', context)
   


def buscador(request):
    data_buscador = request.GET.get('buscador','')
    producto  = Materiales.objects.select_related('categoria').filter(Q(nombre__icontains=data_buscador) | Q(codigo__icontains=data_buscador) |  Q(marca__icontains=data_buscador))
    producto = paginador_general(request, producto)
    context={
        'data':producto
        
    }
    return  render(request, 'pedidos/index.html', context)


def realizar_pedido(request, id_material):
    id_usuario= request.user.id
    if request.method =='POST':
        formulario=  Formualrio_pedido(request.POST)
        if formulario.is_valid():
            usuario = get_object_or_404(Usuario, id=id_usuario)
            material = get_object_or_404(Materiales, id=id_material)
            pedido = formulario.save(commit=False)
            pedido.usuario=usuario
            pedido.material= material
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

def mis_pedidos(request):
    dia_actual = datetime.now()
    id_usuario= request.user.id
    pedidos= Pedido.objects.select_related('usuario', 'material').filter(usuario_id=id_usuario, fecha_pedido__date=dia_actual).order_by('-fecha_pedido')
    context={
        'data':pedidos,
        'title':'Mis pedidos'
    }
    return render(request, 'pedidos/mis_pedidos.html', context)

def todos_mis_pedidos(request):
    id_usuario= request.user.id
    pedidos= Pedido.objects.select_related('usuario', 'material').filter(usuario_id=id_usuario).order_by('-fecha_pedido')
    context={
        'data':pedidos,
        'title':'Historial de pedidos'
    }
    return render(request, 'pedidos/mis_pedidos.html', context)

def listar_pedidos_unidad(request):
    usuario= request.user
    if  usuario.encargado_unidad:
        pedidos_unidad= Pedido.objects.select_related('usuario','material').filter(usuario__secretaria=usuario.secretaria.id)
        context={
        'data':pedidos_unidad
        }

   
        return render(request, 'pedidos/listar_pedidos_unidad.html',context)
    else:
        return HttpResponse("no estas autorizado")
    
def autorizar_pedidos(request, id_pedido):
    print(id_pedido)
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    pedido.estado_autorizacion= True
    pedido.save()
    return HttpResponse("autorizado")