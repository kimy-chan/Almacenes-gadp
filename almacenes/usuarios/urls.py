from django.urls import path, include 
from .views  import login, logout_view, creando_usuario
urlpatterns = [

    path("", login, name="login"),
    path("creando_usuarios", creando_usuario, name="creando_usuarios"),
    path("logout", logout_view, name='logout')
]