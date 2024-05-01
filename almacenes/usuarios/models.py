
from django.contrib.auth.models import AbstractBaseUser , UserManager, PermissionsMixin
from django.dispatch import receiver
from django.db.models.signals import post_migrate
from django.db import models
from ..persona.models import Persona




class Secretaria(models.Model):
    secretaria = models.CharField(max_length=100, blank=True , null=True) 
    @receiver(post_migrate)
    def crear_secreatria_por_defecto (sender, **kwargs) -> str:#crea sin secrearia por defecto
        if sender.name == 'almacenes.usuarios':
            if not Secretaria.objects.exists():
                Secretaria.objects.create(secretaria='Sin secretaria')
        
        
class Usuario(AbstractBaseUser, PermissionsMixin):
    ROLES = [
    ('user', 'Usuario'),
    ('admin', 'Administrador'),
    ]

    username= models.CharField(max_length=150, unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    email=models.EmailField(max_length=255)
    item = models.CharField(max_length=100)
    is_staff= models.CharField(default=True)
    rol = models.CharField(max_length=100, choices=ROLES, default='user')
    cargo = models.CharField(max_length=255, blank=False , null=False)
    secretaria = models.ForeignKey(Secretaria, on_delete=models.CASCADE)
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 
    
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol']

    def __str__(self) -> str:
        return f"{self.rol}"