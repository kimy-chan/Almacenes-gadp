from django import forms
from .models import Pedido

class Formualrio_pedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['descripcion','unidad_manejo','cantidad_pedido']
        widgets = {
            'descripcion': forms.Textarea(attrs={'class': 'form-control','rows':4}),
            'unidad_manejo': forms.TextInput(attrs={'class': 'form-control'}),
            'cantidad_pedido': forms.TextInput(attrs={'class': 'form-control'}),
        }

        
