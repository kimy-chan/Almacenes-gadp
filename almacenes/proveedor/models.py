from django.db import models

from  ..persona.models import Persona, Fechas

class Proveedor(Fechas):
    empresa= models.CharField(max_length=100)
    nit = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=255)
    pais = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.id} {self.empresa}, {self.nit}, {self.telefono}, {self.correo}, {self.pais}, {self.direccion}, {self.fecha_creation}"
    