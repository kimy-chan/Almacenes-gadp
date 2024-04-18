from django.urls import path, include 
from .views  import creando_usarios, logout_view
urlpatterns = [

    path("", creando_usarios, name="login"),
    path("logout", logout_view, name='logout')
]