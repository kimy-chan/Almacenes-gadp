from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Secretaria,Usuario
class Usuario_formulario(forms.ModelForm):
    confirmar_password= forms.CharField(label='confirmar contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}) )
    class Meta:
        model=Usuario
        fields=['username','password','confirmar_password','email', 'item', 'rol','secretaria','cargo']
        widgets={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'rol': forms.Select(attrs={'class': 'form-control'}),
            'item': forms.TextInput(attrs={'class': 'form-control'}),
            'confirmar_password':forms.PasswordInput(attrs={'class': 'form-control'}),
            'cargo':forms.TextInput(attrs={'class': 'form-control'})
        }
       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['secretaria'].widget= forms.Select(attrs={'class': 'form-select'}, choices=[(secretaria.id,secretaria.secretaria) for secretaria in Secretaria.objects.all()])
        
    
    def clean(self):
        clean_data= super().clean()
        password = clean_data.get('password')
        confirmar_password=clean_data.get('confirmar_password')
        if(password != confirmar_password):
            self.add_error('confirmar_password', 'Las contraseñas no son iguales')

        