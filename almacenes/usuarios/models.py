
from django.contrib.auth.models import AbstractBaseUser , UserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.db import models
from ..persona.models import Persona




class Secretaria(models.Model):
    secretaria = models.CharField(max_length=100, blank=False , null=False, unique=True) 

    @receiver(post_migrate)
    def crear_secreatria_por_defecto (sender, **kwargs) -> str:#crea sin secrearia por defecto
        if sender.name == 'almacenes.usuarios':
            if not Secretaria.objects.exists():
                Secretaria.objects.create(secretaria='Sin secretaria')
    def __str__(self) -> str:
        return f"{self.secretaria}"
    
class Roles(models.Model):
    nombre_rol=models.CharField(max_length=100,blank=False, null=False, unique=True)
    def __str__(self) -> str:
        return f"{self.nombre_rol}"  
    
class Usuario(AbstractBaseUser, PermissionsMixin):
    ENCARGADO=[
        ('Encargado','Encargado'),
        ('Personal','Personal')
    ]
    username= models.CharField(max_length=150, unique=True, blank=False, null=False, verbose_name='Usuario')
    password = models.CharField(max_length=128, blank=False, null=False, verbose_name='Contraseña')
    email=models.EmailField(max_length=255, blank=True, null=True)
    item = models.CharField(max_length=100, blank=True, null=True)
    is_staff= models.CharField(default=True)
    rol = models.ForeignKey(Roles, blank=False, null=False, on_delete=models.CASCADE)
    encargado_secretaria=models.CharField( blank=False, null=False, choices=ENCARGADO,default=False, verbose_name='Jefe  de la secretaria' ) 
    encargado_unidad= models.CharField( blank=False, null=False, choices=ENCARGADO,default=False ,verbose_name='Jefe de la unidad' )
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE, blank=False, null=True)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol']

  