from django.urls import path
from .views import crear_categoria, crear_producto
urlpatterns = [
    path('crear_categoria', crear_categoria, name='crear_categoria'),
      path('crear_producto', crear_producto, name='crear_producto')    
]