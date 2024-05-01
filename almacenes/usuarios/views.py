from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages
from django.urls import reverse
from django.db import IntegrityError
from django.core.exceptions import ValidationError
from .forms import Usuarios_formulario
from django.db import transaction
from ..persona.models import Persona 
from .models import Usuario,Secretaria

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
    mensaje_error=None
    if(request.method=="POST"):
        formulario = Usuarios_formulario(request.POST)
        if formulario.is_valid():

            cedula_identidad = formulario.cleaned_data['cedula_identidad']
            nombre = formulario.cleaned_data['nombre']
            apellidos = formulario.cleaned_data['apellidos']
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password']
            email = formulario.cleaned_data['email']
            item = formulario.cleaned_data['item']
            rol = formulario.cleaned_data['rol']   
            secretaria = formulario.cleaned_data['secretaria']
            secretaria = get_object_or_404(Secretaria,id=secretaria)
            try:
                with transaction.atomic():
                    persona = Persona.objects.create(cedula_identidad= cedula_identidad, nombre= nombre, apellidos=apellidos)
                    Usuario.objects.create_user(username=username, password=password , email=email, item=item, rol=rol, persona=persona, secretaria=secretaria)
                    messages.success(request, 'Usuario creado')
                    return redirect(reverse("creando_usuarios"))
            except IntegrityError as e:
                    mensaje_error="El usuario ya existe" 
            except  ValidationError as error:
                    mensaje_error ='Error del  500'                        
    else:
        formulario= Usuarios_formulario()
        mensaje_error=None
    context={'form':formulario,'mensaje_error':mensaje_error}
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
