from django.shortcuts import render, redirect
from django_countries import countries ##sale de aqui todos los paises
from .models import Persona, Proveedor

def formulario_proveedor(request):
    if(request.method == 'POST'):
        empresa = request.POST['empresa']
        nit = request.POST['nit']
        nombre = request.POST['nombre']
        apellidos = request.POST['apellidos']
        cedula_identidad = request.POST['cedula_identidad']
        correo = request.POST['correo']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        pais = request.POST['pais'] 
      
       
        persona= Persona.objects.create(cedula_identidad= cedula_identidad, nombre= nombre, apellidos= apellidos)
        Proveedor.objects.create(empresa=empresa, nit= nit, correo= correo, telefono=telefono,pais=pais ,direccion= direccion, persona=persona)
       
        
        return redirect('proveedor')
    return  render(request, 'proveedores/formulario.html', {'paises':countries})
def actulizar_proveedor(request):
    return render(request,'proveedores/actualizar.formulario.html' )
