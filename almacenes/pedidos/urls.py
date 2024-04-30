from django.urls import path
from .views import index, buscador, realizar_pedido

urlpatterns = [
 path('index',index , name='index' ),
  path('buscar',buscador , name='buscar' ),
    path('realizar_pedido',realizar_pedido , name='realizar_pedido' )
]