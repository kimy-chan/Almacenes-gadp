
from django.shortcuts import HttpResponse, render,HttpResponseRedirect
from .forms import Formulario_papeles
from django.contrib.auth.decorators import login_required

# Create your views here.

def listar_productos_paleles(request):
    return HttpResponse("hola")

def crear_papeles(request):

    form = Formulario_papeles()
    return render(request, "productos/formulario.papeles.html",{'form':form})