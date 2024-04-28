from django.shortcuts import render
from almacenes.productos.models import Productos


def index(request):
    if (request.method == 'POST'):
        id_categoria = request.POST['categoria_id']
        productos_categoria= Productos.objects.select_related('categoria').filter(categoria_id=id_categoria)
    else:
        productos_categoria= Productos.objects.select_related('categoria').all()
    context ={
        'productos':productos_categoria
    }
    return render(request, 'pedidos/index.html', context)
