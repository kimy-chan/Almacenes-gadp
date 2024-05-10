from django.urls import path
from .views import index, buscador, realizar_pedido, listar_pedidos, informacion_pedido, mis_pedidos,todos_mis_pedidos, listar_pedidos_unidad, autorizar_pedidos

urlpatterns = [
 path('index',index , name='index' ),
  path('buscar',buscador , name='buscar' ),
  path('realizar_pedido/<int:id_material>',realizar_pedido , name='realizar_pedido' ),
    path('listando_pedidos',listar_pedidos , name='listando_pedidos' ),
     path('informacion_pedido/<int:id_usuario>',informacion_pedido , name='informacion_pedido' ),
    path('mis_pedidos',mis_pedidos , name='mis_pedidos' ),
        path('todos_mis_pedidos',todos_mis_pedidos, name='todos_mis_pedidos' ),
        path('listar_pedidos_unidad',listar_pedidos_unidad, name='listar_pedidos_unidad' ),
           path('autorizar_pedido/<int:id_pedido>',autorizar_pedidos, name='autorizar_pedido' ),

]