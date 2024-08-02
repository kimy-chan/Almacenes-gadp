from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth.decorators import   login_required
from .forms import Formualrio_pedido
from almacenes.materiales.models import Materiales
from django.db.models import Q
from almacenes.utils.paginador import paginador_general
from almacenes.usuarios.models import Usuario
from almacenes.utils.paginador import paginador_general
from django.urls import reverse
from datetime import datetime
from django.template.loader import render_to_string
from xhtml2pdf import pisa
import os


from .models import Pedido, Autorizacion_pedido

def index(request):
    nombre_categoria='materiales'
    if (request.method == 'POST'):
        id_categoria = request.POST.get('categoria_id')
        if not id_categoria:
            return redirect('index')
        productos_categoria= Materiales.objects.select_related('categoria').filter(categoria_id=id_categoria, es_habilitado=True)
        productos_categoria= paginador_general(request,productos_categoria)
        if productos_categoria and productos_categoria[0].categoria.nombre:
            nombre_categoria = productos_categoria[0].categoria.nombre
        else:
            nombre_categoria = 'materiales'


    else:
        productos_categoria= Materiales.objects.select_related('categoria').filter(es_habilitado=True)
        productos_categoria= paginador_general(request, productos_categoria)
            
    context ={
            'data':productos_categoria,
            'categoria':nombre_categoria
         
                }
    return render(request, 'pedidos/index.html', context)
   


def buscador(request):
    nombre_categoria = 'materiales'
    data_buscador = request.GET.get('buscador','')
    producto  = Materiales.objects.select_related('categoria').filter(Q(nombre__icontains=data_buscador) | Q(codigo__icontains=data_buscador) |  Q(marca__icontains=data_buscador), es_habilitado= True)
    producto = paginador_general(request, producto)
    context={
        'data':producto,
        'categoria':nombre_categoria
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
        'material':get_object_or_404(Materiales,pk=id_material),
        'forms': formulario
    }
    return render(request , 'pedidos/realizar_pedido.html', context)

def listar_pedidos(request):
    listando_pedidos = Pedido.objects.filter(aprobado_unidad=True).distinct('usuario')
    context={
       'data':listando_pedidos
    }
    return render(request, 'pedidos/listar_pedido.html', context)

def listando_pedido_almacen(request, id_usuario):
    pedido = Pedido.objects.filter(aprobado_unidad=True, usuario=id_usuario)       
    context = {
        'data': pedido
        }
    return render(request, 'pedidos/lintando.pedidos.almacen.html', context)

def lista_pedido_por_id(request, id_pedido):
    pedido=get_object_or_404(Pedido, pk= id_pedido)
    data ={
        'id':pedido.id,
        'codigo':pedido.material.codigo,
        'nombre': pedido.material.nombre,
        'cantidad': pedido.cantidad_pedida
        
    }
    return JsonResponse({'data':data})

def realizar_entrega(request):
    if request.method == 'POST':
        id= request.POST['pedido_id']
        cantidad_entregada = request.POST['cantidad_entregada']
        pedido = get_object_or_404(Pedido,pk= id)
        if int(cantidad_entregada) > pedido.cantidad_pedida:
            return JsonResponse({'data':'Cantidad excedida'})
        elif  cantidad_entregada==pedido.cantidad_pedida:
            pedido.estado_pedido_almacen ='Completada'
        elif int(cantidad_entregada) < pedido.cantidad_pedida:
            pedido.estado_pedido_almacen ='Incompleto'
        pedido.cantidad_entrega = cantidad_entregada
        pedido.save()
        return JsonResponse({'data':'recivido'})


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
        print(aprobaciones)
        for aprobacion in aprobaciones:
            informacion ={
            'secretaria':aprobacion.usuario.unidad.nombre,
            'aprobacion':aprobacion.estado_autorizacion,
            'nombre':aprobacion.usuario.persona.nombre + " " + aprobacion.usuario.persona.apellidos ,
            'area':aprobacion.usuario.unidad.nombre,
            'fecha': aprobacion.fecha_de_autorizacion.strftime('%Y-%m-%d') if aprobacion.fecha_de_autorizacion else None
            }
            data.append(informacion)
        print(data)
        return JsonResponse({'data':data})

def eliminar_mi_pedido(request, id_pedido):
    pedido= get_object_or_404(Pedido, pk=id_pedido)
    pedido_autorizado = Autorizacion_pedido.objects.filter(pedido=pedido)
    for p in pedido_autorizado:
        if p.estado_autorizacion == True:
            return redirect(f"{reverse('mis_pedidos')}?error=Este pedido ha sido aprobado y no se puede cancelar")
        continue
    pedido.delete()
    return redirect(f"{reverse('mis_pedidos')}?success=Pedido cancelado correctamente")

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
    if usuario.encargado== False:
        return JsonResponse({"mensage" :"no tienes permispo"})
    pedidos_unidad= Pedido.objects.select_related('usuario','material').filter(
        usuario__unidad=usuario.unidad.id)
    pedidos_unidad= paginador_general(request, pedidos_unidad)
   
    context={
        'data':pedidos_unidad
        }
    return render(request, 'pedidos/listar_pedidos_unidad.html',context)
    
    
def autorizar_pedidos(request, id_pedido):#autoria el pedido de cada unidad
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    usuario = get_object_or_404(Usuario, pk= id_usuario)
    autorizacion_pedido= Autorizacion_pedido.objects.create(pedido=pedido,usuario= usuario, estado_autorizacion= True)
    autorizacion_pedido.save()
    pedido.aprobado_unidad= True
    pedido.save()
    return redirect(f"{reverse('listar_pedidos_unidad', kwargs={'id_usuario': id_usuario})}?success=Pedido autorizado correctamente")

def autorizar_pedidos_almacen(request, id_pedido, id_usuario):#autoriza pedidos el lamacen
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    usuario = get_object_or_404(Usuario, pk= id_usuario)
    autorizacion_pedido= Autorizacion_pedido.objects.create(pedido=pedido,usuario= usuario, estado_autorizacion= True)
    autorizacion_pedido.save()
    pedido.aprobado_almacen= True
    pedido.save()
    return redirect(f"{reverse('informacion_pedido', kwargs={'id_usuario': id_usuario})}?success=Pedido autorizado correctamente")




def rechazar_pedido_unidad(request, id_pedido):
    id_usuario= request.user.id
    pedido = get_object_or_404(Pedido,pk=id_pedido)
    pedido.aprobado_unidad= False
    pedido.save()
    usuario = get_object_or_404(Usuario, pk= id_usuario)
    autorizacion_pedido= Autorizacion_pedido.objects.create(pedido=pedido,usuario= usuario, estado_autorizacion= False)
    autorizacion_pedido.save()
    
    return redirect(f"{reverse('listar_pedidos_unidad', kwargs={'id_usuario': id_usuario})}?pedido_rechazado=Pedido rechazado correctamente")
    




def imprecion_solicitud(request,id_pedido):
    pedido= get_object_or_404(Pedido,pk=id_pedido)
    context = {
        'pedido': pedido
    }
    return render(request, "imprimir/solicitud.html", context)


def generate_pdf(request, id_pedido):
    pedido= get_object_or_404(Pedido,pk=id_pedido)
    context = {
        'pedido': pedido
    }
    html_string = render_to_string('imprimir/imprimir.html', context)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="pedido_materiales.pdf"'
    pisa_status = pisa.CreatePDF(html_string, dest=response)
    if pisa_status.err:
        return HttpResponse('Error generating PDF', status=500)
    return response
   