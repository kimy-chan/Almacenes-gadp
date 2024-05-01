from django.urls import path
from .views import index, buscador, realizar_pedido, listar_pedidos, informacion_pedido

urlpatterns = [
 path('index',index , name='index' ),
  path('buscar',buscador , name='buscar' ),
  path('realizar_pedido/<int:id_producto>',realizar_pedido , name='realizar_pedido' ),
    path('listando_pedidos',listar_pedidos , name='listando_pedidos' ),
     path('informacion_pedido/<int:id_usuario>',informacion_pedido , name='informacion_pedido' )
]