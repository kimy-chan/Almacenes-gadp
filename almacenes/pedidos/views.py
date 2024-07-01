from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import   login_required
from .forms import Formualrio_pedido
from almacenes.materiales.models import Materiales
from django.db.models import Q
from almacenes.utils.paginador import paginador_general
from almacenes.usuarios.models import Usuario
from almacenes.utils.paginador import paginador_general
from datetime import datetime

from .models import Pedido, Autorizacion_pedido

def index(request):
    if (request.method == 'POST'):
        id_categoria = request.POST.get('categoria_id')
        if not id_categoria:
            return redirect('index')
        productos_categoria= Materiales.objects.select_related('categoria').filter(categoria_id=id_categoria, es_habilitado=True)
        productos_categoria= paginador_general(request,productos_categoria)
    else:
        productos_categoria= Materiales.objects.select_related('categoria').filter(es_habilitado=True)
        productos_categoria= paginador_general(request, productos_categoria)
    context ={
            'data':productos_categoria,
         
                }
    return render(request, 'pedidos/index.html', context)
   


def buscador(request):
    data_buscador = request.GET.get('buscador','')
    producto  = Materiales.objects.select_related('categoria').filter(Q(nombre__icontains=data_buscador) | Q(codigo__icontains=data_buscador) |  Q(marca__icontains=data_buscador), es_habilitado= True)
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
    datos_pedidos = Pedido.objects.select_related('usuario', 'producto').filter(usuario_id=id_usuario)
    datos_pedidos[0].usuario.persona.nombre
    for x in datos_pedidos:
        print(x.descripcion)
    context={
        'data': datos_pedidos
    }
    return render(request, 'pedidos/informacion_pedidos.html', context)

def mis_pedidos(request): #muestra los pedidos de cada unidad o secretaria
    id_usuario= request.user.id
    pedidos= Pedido.objects.select_related('usuario').filter(usuario_id=id_usuario).order_by('-fecha_pedido')   
    pedidos= paginador_general(request, pedidos)
    context={
        'data':pedidos,
        'title':'Mis pedidos'
    }
    return render(request, 'pedidos/mis_pedidos.html', context)

def mostrar_informacion_pedidio_aprobaciones(request,id_pedido):
    if request.method == 'GET':
        data=[]
        pedido = get_object_or_404(Pedido, pk=id_pedido)
        aprobaciones = Autorizacion_pedido.objects.filter(pedido= pedido.id)
        for aprobacion in aprobaciones:
            print(aprobacion)
            informacion ={
            'secretaria':aprobacion.usuario.secretaria.secretaria,
            'aprobacion':aprobacion.estado_autorizacion,
            'nombre':aprobacion.usuario.persona.nombre + " " + aprobacion.usuario.persona.apellidos ,
            'area':aprobacion.usuario.area_trabajo.nombre_area,
            }
            data.append(informacion)
             
        return JsonResponse({'data':data})

def eliminar_mi_pedido(request, id_pedido):
    pedido= get_object_or_404(Pedido, pk=id_pedido)
    pedido.delete()
    return redirect('mis_pedidos')

def todos_mis_pedidos(request):
    id_usuario= request.user.id
    print(id_usuario)
    pedidos= Pedido.objects.select_related('usuario', 'material').filter(usuario_id=id_usuario).order_by('-fecha_pedido')
    context={
        'data':pedidos,
        'title':'Historial de pedidos'
    }
    return render(request, 'pedidos/mis_pedidos.html', context)

def listar_pedidos_unidad(request, id_usuario): #esta suelto no esta en uso
    usuario = get_object_or_404(Usuario, pk=id_usuario)
    pedidos_unidad= Pedido.objects.select_related('usuario','material').filter(
        usuario__secretaria=usuario.secretaria.id
        ,estado_pedido=False, 
        estado_autorizacion_unidad=True)
    print(pedidos_unidad)
    pedidos_unidad= paginador_general(request, pedidos_unidad)
    context={
        'data':pedidos_unidad
        }
    return render(request, 'pedidos/listar_pedidos_unidad.html',context)
    
    
def autorizar_pedidos(request, id_pedido):#autoria el pedido de cada secretaria
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    usuario = get_object_or_404(Usuario, pk= id_usuario)
    autorizacion_pedido= Autorizacion_pedido.objects.create(pedido=pedido,usuario= usuario, estado_autorizacion= True)
    autorizacion_pedido.save()
    return  redirect('listar_pedidos_secretarias', id_usuario)

def autorizar_pedidos_unidad_mayor(request, id_pedido):
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    pedido.estado_autorizacion_unidad= True
    pedido.fecha_de_autorizacion= datetime.now()
    pedido.save()
    return  redirect('listar_pedidos_unidad', id_usuario)

def rechazar_pedido(request, id_pedido):
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    usuario = get_object_or_404(Usuario, pk= id_usuario)
    autorizacion_pedido= Autorizacion_pedido.objects.create(pedido=pedido,usuario= usuario, estado_autorizacion= False)
    autorizacion_pedido.save()
    return  redirect('listar_pedidos_secretarias', id_usuario)

def rechazar_pedido_unidad_mayor(request, id_pedido):
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    pedido.estado_pedido_unidad_mayor_rechazar= True
    pedido.save()
    return  redirect('listar_pedidos_unidad', id_usuario)


  
def listar_Pedidos_secretarias(request, id_usuario):
    usuario= get_object_or_404(Usuario, pk=id_usuario)
    pedidos_secretaria= Pedido.objects.select_related('usuario','material').filter(usuario__secretaria=usuario.secretaria.id)
    pedidos_secretaria = paginador_general(request, pedidos_secretaria)
    context={
        'data':pedidos_secretaria
        }
    return render(request, 'pedidos/listar_pedidos.html',context)