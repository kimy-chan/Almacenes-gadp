
from django.contrib.auth.models import AbstractBaseUser , UserManager, PermissionsMixin
from django.db import models
from ..persona.models import Persona



ROLES = [
    ('user', 'Usuario'),
    ('admin', 'Administrador'),
]

class Usuario(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email=models.EmailField(max_length=255)
    item = models.CharField(max_length=100)
    is_staff= models.CharField(default=True)
    rol = models.CharField(max_length=100, choices=ROLES, default='user')
    person = models.ForeignKey(Persona, on_delete=models.CASCADE, null= True) 
    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol']