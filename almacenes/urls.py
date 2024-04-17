
from django.urls import path, include 
urlpatterns = [
    path('proveedor/' ,include('almacenes.proveedor.urls'))#urls proveedor
    
]
