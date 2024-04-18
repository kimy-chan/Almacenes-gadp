
from django.urls import path, include 
urlpatterns = [
    path('proveedor/' ,include('almacenes.proveedor.urls')),#urls proveedor
    path('productos/' ,include('almacenes.productos.urls')),#urls productos
    path('', include('almacenes.usuarios.urls'))
    
    
]
