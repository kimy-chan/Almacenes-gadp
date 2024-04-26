from almacenes.productos.models import Categoria

def listado_categorias_sidebar(request):
    categoria= Categoria.objects.all()
    return  {'categoria_sidebar':categoria}