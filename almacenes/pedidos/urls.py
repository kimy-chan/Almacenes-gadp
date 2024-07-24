from django.urls import path
from .views import index, imprecion_solicitud,autorizar_pedidos_almacen,generate_pdf,buscador,mostrar_informacion_pedidio_aprobaciones, realizar_pedido, listar_pedidos, informacion_pedido, mis_pedidos,todos_mis_pedidos, listar_pedidos_unidad, autorizar_pedidos, listar_Pedidos_secretarias, rechazar_pedido, eliminar_mi_pedido, autorizar_pedidos_unidad_mayor, rechazar_pedido_unidad_mayor

urlpatterns = [
   path('index',index , name='index' ),
   path('buscar',buscador , name='buscar' ),
   path('realizar_pedido/<int:id_material>',realizar_pedido , name='realizar_pedido' ),
   path('listando_pedidos',listar_pedidos , name='listando_pedidos' ),
   path('informacion_pedido/<int:id_usuario>',informacion_pedido , name='informacion_pedido' ),
   path('mis_pedidos',mis_pedidos , name='mis_pedidos' ),
   path('todos_mis_pedidos',todos_mis_pedidos, name='todos_mis_pedidos' ),
   path('listar_pedidos_unidad/<int:id_usuario>',listar_pedidos_unidad, name='listar_pedidos_unidad' ),
   path('autorizar_pedido/<int:id_pedido>',autorizar_pedidos, name='autorizar_pedido' ),
   path('autorizar_pedido_almacen/<int:id_pedido>',autorizar_pedidos_almacen, name='autorizar_pedido_almacen' ),

      
   path('rechazar_pedido/<int:id_pedido>',rechazar_pedido, name='rechazar_pedido' ),
   path('rechazar_pedidos_unidad_mayor/<int:id_pedido>',rechazar_pedido_unidad_mayor, name='rechazar_pedidos_unidad_mayor' ),
   path('eliminar_mi_pedido/<int:id_pedido>',eliminar_mi_pedido, name='eliminar_mi_pedido'),
   path('listar_pedidos_secretarias/<int:id_usuario>',listar_Pedidos_secretarias, name='listar_pedidos_secretarias' ),
   path('informacion/pedido/<int:id_pedido>' , mostrar_informacion_pedidio_aprobaciones , name="info_aprobaciones" ),
   path('imprimir/<int:id_pedido>',imprecion_solicitud, name='imprimir' ),
   path('generar/pdf/<int:id_pedido>',generate_pdf, name='pdf' )
   
]