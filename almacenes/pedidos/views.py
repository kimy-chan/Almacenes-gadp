from django.shortcuts import render
from .models import Usuario


def index(request):
    id_user= request.user.id
    usuario_rol = Usuario.objects.filter(pk=id_user)
    context={
        'usuario_rol':usuario_rol

    }
    return render(request, 'pedidos/index.html',context)