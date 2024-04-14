from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class Fechas(models.Model):
    fecha_creation= models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True
    

class Persona(Fechas):
    cedula_identidad= models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos= models.CharField(max_length=60)

class Proveedor(Fechas):
    empresa= models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=255)
    pais = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.pais
    

  
class User(AbstractUser):
    person= models.ForeignKey(Persona, on_delete=models.CASCADE, null=True)



 


    