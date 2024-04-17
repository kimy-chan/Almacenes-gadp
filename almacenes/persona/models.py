from django.db import models
from django.utils import timezone

class Fechas(models.Model):
    fecha_creation= models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True
    

class Persona(Fechas):
    cedula_identidad= models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos= models.CharField(max_length=60)

    def __str__(self) -> str:
        return f"{self.cedula_identidad},{self.nombre}, {self.apellidos},{self.fecha_creation}"      