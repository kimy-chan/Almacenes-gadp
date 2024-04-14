
from django.urls import path
from  almacenes.proveedores_views import formulario_proveedor, actulizar_proveedor
 
urlpatterns = [
    ##urls de proveedors
    path('proveedor', formulario_proveedor, name='proveedor'),
    path('actualizar_proveedor' , actulizar_proveedor, name='actualizar_proveedor')

    ## urls de pedidos
    
]
