from django.urls import path, include 
from .views  import login_sistema, logout_view, creando_usuario, listando_usuarios, crear_secretaria
urlpatterns = [

    path("", login_sistema, name="login"),
    path("creando_usuarios", creando_usuario, name="creando_usuarios"),
    path('listando_usuarios',listando_usuarios,name='listando_usuarios' ),
    path('crear_secretaria',crear_secretaria,name='crear_secretaria' ),

    path("logout", logout_view, name='logout')
]