from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, logout, login
from django.db import IntegrityError
from django.urls import reverse
from .forms import Usuario_formulario

from .models import Usuario, Secretaria, Area_trabajo
from django.http import JsonResponse

from almacenes.persona.forms import formulario_persona 

from almacenes.utils.paginador import paginador_general

# Create your views here.

def login_sistema(request):
    if(request.method=='POST'):
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


def crear_secretaria_listar(request):
    if(request.method == 'POST'):
        secretaria_post = request.POST.get('secretaria','').strip() 
        if not secretaria_post:
             return JsonResponse({"error":'este campo es obligatorio'})
        try:
            secretaria = Secretaria(secretaria=secretaria_post)
            secretaria.save()
            return JsonResponse({"data": True})
        except IntegrityError:
            return JsonResponse({"error": "El valor  ya existe"})

    else:
        secretatias = list(Secretaria.objects.all().values())   
        return JsonResponse({'data':secretatias}, safe=False)

def crear_aras_trabajo_listar(request):
    if(request.method == 'POST'):
        try:
            nombre_area= request.POST['nombre_area']
            if not nombre_area:
                return JsonResponse({'error':'Este campo es obligatorio'})
            nombre_area= Area_trabajo(nombre_area= nombre_area)
            nombre_area.save()
            return JsonResponse({'data':True})
        except IntegrityError:
            return JsonResponse({"error": "El valor  ya existe"})
    else:
        area_trabajo = list(Area_trabajo.objects.all().values())
        return JsonResponse({'data':area_trabajo})
    
def listando_usuarios(request):
    listado_cuentas_usuarios = Usuario.objects.select_related('persona').all()

    listado_cuentas_usuarios = paginador_general(request, listado_cuentas_usuarios)
    context={
        'data':listado_cuentas_usuarios,
       
    }
    return render(request, 'usuarios/mostrar_cuentas.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')
