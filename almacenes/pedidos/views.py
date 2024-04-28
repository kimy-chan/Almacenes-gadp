from django.shortcuts import render
from almacenes.productos.models import Productos
from django.db.models import Q
from almacenes.utils.paginador import paginador_general



def index(request):
    if (request.method == 'POST'):
        id_categoria = request.POST['categoria_id']
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