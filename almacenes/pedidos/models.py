from django.db import models
from  ..usuarios.models import Usuario
from ..productos.models import Productos
class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES=[
        ('Pendiente','Pendiente'),
        ('Incompleto','Incompleto'),
        ('Completo','Completo')
    ]

    descripcion =models.TextField()
    unidad_manejo=models.IntegerField()
    cantidad_pedido=models.IntegerField()
    entrega_almacen=models.IntegerField()
    precio_paquete= models.DecimalField(max_digits=10, decimal_places=2)
    total=models.DecimalField(max_digits=10, decimal_places=2)
    estado_pedido = models.CharField(choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')
    usuario=models.ForeignKey(Usuario , models.CASCADE)
    productos= models.ManyToManyField(Productos, through='DetallePedido')

    REQUIRED_FIELDS = ['estado_pedido']



class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)