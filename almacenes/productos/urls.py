from django.urls import path
from .views import crear_categoria, crear_producto, listado_productos,informacion_producto
urlpatterns = [
    path('crear_categoria', crear_categoria, name='crear_categoria'),
      path('crear_producto', crear_producto, name='crear_producto'), 

    path('<int:id_categoria>', listado_productos, name='categorias_por_id'),  #ruta para listar los prodcutos por categoria  
    path('informacion/<int:id_producto>',informacion_producto, name='informacion_producto' )
]