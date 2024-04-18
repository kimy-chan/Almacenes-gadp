from django import forms

from django import forms

class Formulario_papeles(forms.Form):
    nombre = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    codigo = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    marca = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    cantidad = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    codigo_clasificacion = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    tamaño = forms.CharField(max_length=255, widget=forms.TextInput(attrs={'class': 'form-control'}))
    color = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))

      
 