from django.urls import path
from .views import index, buscador

urlpatterns = [
 path('index',index , name='index' ),
  path('buscar',buscador , name='buscar' )
]