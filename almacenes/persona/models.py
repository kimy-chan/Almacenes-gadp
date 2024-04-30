from django.db import models
from django.utils import timezone


class Persona(models.Model):
    cedula_identidad= models.CharField(max_length=20 ,blank=False, null=False)
    nombre = models.CharField(max_length=50, blank=False, null=False)
    apellidos= models.CharField(max_length=60,blank=False, null=False)
    fecha_creacion= models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.cedula_identidad},{self.nombre}, {self.apellidos},{self.fecha_creacion}"      