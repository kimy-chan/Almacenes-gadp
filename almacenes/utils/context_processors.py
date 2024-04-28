from almacenes.productos.models import Categoria
from almacenes.usuarios.models import Usuario

def listado_categorias_sidebar(request):
    categoria= Categoria.objects.all()
    return  {'listado_categoria':categoria}
def user_datos(request):
    usuario_id = request.user.id
    usuario = Usuario.objects.select_related('persona').get(pk=usuario_id)
    return {'usuario':usuario}