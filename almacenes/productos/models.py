from django.db import models


class Categoria(models.Model):
    codigo_clasificacion = models.CharField(max_length=100, unique=True , blank=False, null=False, error_messages={'unique':'El codigo de la categoria ya existe'})
    nombre= models.CharField(max_length=200, blank=False, unique=True, null=False, error_messages={'unique':'El nombre de la categoria ya existe'})
    fecha_creacion= models.DateField(auto_now_add=True)
    def __str__(self) -> str:
        return f"{self.nombre},{self.codigo_clasificacion}, {self.fecha_creacion}"

class Productos(models.Model):
    nombre = models.CharField(max_length=255,blank=False, null=False,)
    codigo = models.CharField(max_length=255, blank=False, null=False, unique=True,  error_messages={'unique':'El codigo de producto ya existe'})
    marca = models.CharField(max_length=255, blank=False, null=False)
    cantidad_unidad = models.IntegerField(blank=False, null=False,verbose_name='Cantidad por unidad')
    cantidad_paquete=models.IntegerField(blank=False, null=False, verbose_name='Cantidad por paquetes')
    precio_unidad = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False,verbose_name='Precio por unidad')
    precio_paquete = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False,verbose_name='Precio por paquetes')
    fecha_creacion = models.DateTimeField(auto_now_add=True, blank=False, null=False)
    tamaño = models.CharField(max_length=255,blank=True, null=True)
    color = models.CharField(max_length=100,blank=True, null=True)
    unidad_medida = models.CharField(max_length=255,blank=True, null=True, verbose_name='Unidad de medida')
    material = models.CharField(max_length=255,blank=True, null=True)
    numero_serie = models.CharField(max_length=255, unique=True, blank=True, null=True,  error_messages={'unique':'El numero de serie de producto ya existe'}, verbose_name='Numero de serie')
    categoria =models.ForeignKey(Categoria, models.CASCADE,blank=False, null=False )

    def __str__(self) -> str:
        return f"""{self.nombre},{self.codigo},{self.marca},
        {self.cantidad_unidad},{self.cantidad_paquete},{self.fecha_creacion},
        {self.tamaño},{self.unidad_medida},{self.material},{self.numero_serie},{self.categoria}"""
