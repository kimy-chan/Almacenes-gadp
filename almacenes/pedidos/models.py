from django.db import models
from  ..usuarios.models import Usuario
from ..productos.models import Productos
class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES=[
        ('Pendiente','Pendiente'),
        ('Incompleto','Incompleto'),
        ('Completo','Completo')
    ]

    ESTADO_AUTORIZACION=[
        ('Autorizado','Autorizado'),
        ('No autorizado','No autorizado'),
    ]
    descripcion =models.TextField(blank=False , null=False)
    unidad_manejo=models.CharField(max_length=20, blank= False ,null= False)
    cantidad_pedido=models.IntegerField(blank=False, null=False)
    cantidad_entrega_almacen=models.IntegerField()
    partida_presupuestada=models.DecimalField(max_digits=10, decimal_places=2)
    estado_autorizacion = models.CharField(choices=ESTADO_AUTORIZACION, default='No autorizado')
    estado_pedido = models.CharField(choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')
    usuario=models.ForeignKey(Usuario , models.CASCADE , blank= False, name=False)
    productos= models.ManyToManyField(Productos, through='DetallePedido', blank= False, name=False)

    REQUIRED_FIELDS = ['estado_pedido']



class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    