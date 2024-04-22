from typing import Any
from django import forms
class Usuarios_formulario(forms.Form):
    mensaje_error='Este campo es obligatorio'
    ROLES = [
    ('user', 'Usuario'),
    ('admin', 'Administrador'),
    ]
 
  
    cedula_identidad = forms.CharField(label='Cedula de Identidad', max_length=20,error_messages={'required': mensaje_error}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre', max_length=50,error_messages={'required': mensaje_error} ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', max_length=60, error_messages={'required': mensaje_error},widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Usuario', max_length=150,error_messages={'required': mensaje_error}, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', max_length=128,error_messages={'required': mensaje_error}, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmar_password = forms.CharField(label='Confirmar Contraseña',error_messages={'required': mensaje_error},max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico', required=False, max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    item = forms.CharField(label='Item', max_length=100,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rol = forms.ChoiceField(choices=ROLES ,error_messages={'required': mensaje_error} , widget=forms.Select(attrs={'class': 'form-control'}))

    def clean(self):
        clean_data= super().clean()
        password = clean_data.get('password')

        confirmar_password=clean_data.get('confirmar_password')
        if(password != confirmar_password):
            self.add_error('confirmar_password', 'Las contraseñas no son iguales')

        