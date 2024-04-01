from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# Create your models here.


class TablesDate(models.Model):
    fecha_creation= models.DateTimeField(default=timezone.now)
    class Meta:
        abstract = True
    


class Person(TablesDate):
    cedulaIdentidad= models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos= models.CharField(max_length=60)
    item= models.CharField(max_length=10)
  
class User(AbstractUser):
    person= models.ForeignKey(Person, on_delete=models.CASCADE)

class Category(TablesDate):
    nombre_categoria=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=255)
    
  
class Product(TablesDate):
    codigo=models.CharField(max_length=15)
    nombre_producto = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=255)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    

 


    