from django.db import models

class Producto_base(models.Model):
    nombre = models.CharField(max_length=255)
    codigo = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    cantidad = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    codigo_clasificacion = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True  #se le ñpone astracto en true para que no se cree la tabla productosbase en la base de datos

class Papeles(Producto_base):
    tamaño = models.CharField(max_length=255)
    color = models.CharField(max_length=100)

class Limpieza(Producto_base):
    unidad_medida = models.CharField(max_length=255)

class Material_escritorio(Producto_base):
    color = models.CharField(max_length=100)
    unidad_medida = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=100)
    material = models.CharField(max_length=255)
    tipo = models.CharField(max_length=255)
    numero_serie = models.CharField(max_length=255)

class Artes_grafias(Producto_base):
    color = models.CharField(max_length=100)
    tamaño = models.CharField(max_length=255)
