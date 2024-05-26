from django.shortcuts import render



def vistar_administracion(request):
    return render(request, 'administracion/administracion.html')
