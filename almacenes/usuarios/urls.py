from django.urls import path, include 
from .views  import login_sistema, logout_view, creando_usuario, listando_usuarios, crear_secretaria_listar, crear_aras_trabajo_listar,soft_delete, activar_cuenta, desactivar_cuenta, actulizar_cuenta_usuario
urlpatterns = [

    path("", login_sistema, name="login"),
    path("creando_usuarios", creando_usuario, name="creando_usuarios"),
    path('listando_usuarios',listando_usuarios,name='listando_usuarios' ),
    path('crear_secretaria_listar',crear_secretaria_listar,name='crear_secretaria_listar' ),
    path('crear_aras_trabajo_listar',crear_aras_trabajo_listar,name='crear_aras_trabajo_listar' ),
    path('eliminar/<int:id>', soft_delete, name='eliminar_cuenta') ,
    path('activar_cuenta/<int:id>', activar_cuenta, name='activar_cuenta') ,
    path('desactivar_cuenta/<int:id>', desactivar_cuenta, name='desactivar_cuenta') ,
    path('actulizar_cuenta_usuario/<int:id_usuario>/<int:id_persona>', actulizar_cuenta_usuario, name='actulizar_cuenta_usuario') ,
    path("logout", logout_view, name='logout')
]