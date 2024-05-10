
from django.urls import path, include 
urlpatterns = [
    path('proveedor/' ,include('almacenes.proveedor.urls')),#urls proveedor
    path('material/' ,include('almacenes.materiales.urls')),#urls materiales
    path('', include('almacenes.pedidos.urls'))
    ,
    path('', include('almacenes.usuarios.urls'))
    
    
]
