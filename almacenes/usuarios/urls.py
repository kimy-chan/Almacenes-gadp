from django.urls import path, include 
from .views  import login_sistema, logout_view, creando_usuario, listando_usuarios, crear_secretaria_listar, crear_aras_trabajo_listar
urlpatterns = [

    path("", login_sistema, name="login"),
    path("creando_usuarios", creando_usuario, name="creando_usuarios"),
    path('listando_usuarios',listando_usuarios,name='listando_usuarios' ),
    path('crear_secretaria_listar',crear_secretaria_listar,name='crear_secretaria_listar' ),
      path('crear_aras_trabajo_listar',crear_aras_trabajo_listar,name='crear_aras_trabajo_listar' ),

    path("logout", logout_view, name='logout')
]