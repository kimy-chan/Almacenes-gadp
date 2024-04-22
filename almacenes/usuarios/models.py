
from django.contrib.auth.models import AbstractBaseUser , UserManager, PermissionsMixin
from django.db import models
from ..persona.models import Persona



ROLES = [
    ('user', 'Usuario'),
    ('admin', 'Administrador'),
]

class Usuario(AbstractBaseUser, PermissionsMixin):
    username= models.CharField(max_length=150, unique=True, blank=False, null=False)
    password = models.CharField(max_length=128, blank=False, null=False)
    email=models.EmailField(max_length=255)
    item = models.CharField(max_length=100)
    is_staff= models.CharField(default=True)
    rol = models.CharField(max_length=100, choices=ROLES, default='user')
    persona = models.ForeignKey(Persona, on_delete=models.CASCADE) 

    
    objects = UserManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['rol']

    def __str__(self) -> str:
        return f"{self.rol}"