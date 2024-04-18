from django.shortcuts import HttpResponse, redirect, render
from django.contrib.auth import authenticate, logout, login


# Create your views here.

def creando_usarios(request):
    if(request.method=='POST'):
        print(request)
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('listar_proveedor')
        else:
              return render(request, 'registration/login.html', {'error_message': 'Credenciales inválidas'})

    else:
         return render(request, 'registration/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')