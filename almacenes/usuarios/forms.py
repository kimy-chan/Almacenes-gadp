from django import forms
from .models import Secretaria
class Usuarios_formulario(forms.Form):
    ROLES = [
    ('user', 'Usuario'),
    ('admin', 'Administrador'),
    ]
   
    cedula_identidad = forms.CharField(label='Cedula de Identidad', max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}))
    nombre = forms.CharField(label='Nombre', max_length=50 ,widget=forms.TextInput(attrs={'class': 'form-control'}))
    apellidos = forms.CharField(label='Apellidos', max_length=60,widget=forms.TextInput(attrs={'class': 'form-control'}))
    username = forms.CharField(label='Usuario', max_length=150,widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Contraseña', max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    confirmar_password = forms.CharField(label='Confirmar Contraseña',max_length=128, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Correo Electrónico', required=False, max_length=255, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    item = forms.CharField(label='Item', max_length=100,required=False, widget=forms.TextInput(attrs={'class': 'form-control'}))
    rol = forms.ChoiceField(choices=ROLES, widget=forms.Select(attrs={'class': 'form-control'}))
    secretaria = forms.ChoiceField(label='Selecionar secretaria', choices=[], widget=forms.Select(attrs={'class': 'form-control'}))
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['secretaria'].choices=[(x.id, x.secretaria) for x in Secretaria.objects.all()]
    
    def clean(self):
        clean_data= super().clean()
        password = clean_data.get('password')
        confirmar_password=clean_data.get('confirmar_password')
        if(password != confirmar_password):
            self.add_error('confirmar_password', 'Las contraseñas no son iguales')
    

        