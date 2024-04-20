from django.db import models


class Categoria(models.Model):
    codigo_clasificacion = models.CharField(max_length=100)
    nombre= models.CharField(max_length=200)

class Productos(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    tamaño = models.CharField(max_length=255)
    color = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=255)
    categoria =models.ForeignKey(Categoria, models.CASCADE)
