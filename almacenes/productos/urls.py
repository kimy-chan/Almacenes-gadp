from django.urls import path
from .views import listar_productos_paleles, crear_papeles
urlpatterns = [
    path('', listar_productos_paleles, name='listar_productos_paleles'),
    path('añadir_papeles', crear_papeles, name='formulario_papeles')   
]