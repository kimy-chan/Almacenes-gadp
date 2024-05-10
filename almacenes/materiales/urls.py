from django.urls import path
from .views import crear_categoria, crear_material, listado_material,informacion_material
urlpatterns = [
    path('crear_categoria', crear_categoria, name='crear_categoria'),
      path('crear_producto', crear_material, name='crear_producto'), 

    path('<int:id_categoria>', listado_material, name='categorias_por_id'),  #ruta para listar los prodcutos por categoria  
    path('informacion/<int:id_material>',informacion_material, name='informacion_material' )
]