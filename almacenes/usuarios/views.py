from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .forms import Usuario_formulario
from django.db import transaction
from ..persona.models import Persona 
from .models import Usuario,Secretaria

from almacenes.persona.forms import formulario_persona

from almacenes.utils.paginador import paginador_general

# Create your views here.

def login_sistema(request):
    if(request.method=='POST'):
        print("hola soy el post")
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            return render(request, 'usuarios/login.html', {'error_message': 'Credenciales inválidas'})
    else:
        return render(request, 'usuarios/login.html')


def creando_usuario(request):
    if(request.method=="POST"):
        formulario_u = Usuario_formulario(request.POST)
        formulario_p = formulario_persona(request.POST)
        if formulario_u.is_valid() and  formulario_p.is_valid():
            persona= formulario_p.save()
            usuario= formulario_u.save(commit=False)
            usuario.set_password(formulario_u.cleaned_data['password'])
            usuario.persona=persona
            usuario.save()
        else:
            formulario_u= Usuario_formulario(request.POST)
            formulario_p = formulario_persona(request.POST)
    else:
        formulario_u= Usuario_formulario()
        formulario_p = formulario_persona()
    context={'form_usuario':formulario_u,
             'form_persona':formulario_p,
             }
    return render(request, 'usuarios/crear_cuenta_formulario.html', context)

def listando_usuarios(request):
    listado_cuentas_usuarios = Usuario.objects.select_related('persona').all()
    listado_cuentas_usuarios = paginador_general(request, listado_cuentas_usuarios)
    context={
        'data':listado_cuentas_usuarios
    }
    return render(request, 'usuarios/mostrar_cuentas.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
