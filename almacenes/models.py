from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Person(models.Model):
    cedulaIdentidad= models.CharField(max_length=20)
    nombre = models.CharField(max_length=50)
    apellidos= models.CharField(max_length=60)
    item= models.CharField(max_length=10)
  
class User(AbstractUser):
    person= models.ForeignKey(Person, on_delete=models.CASCADE)
  
class Product(models.Model):
    pass

class category(models.Model):
    pass