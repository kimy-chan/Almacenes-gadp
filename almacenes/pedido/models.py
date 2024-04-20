from django.db import models
from  ..usuarios.models import Usuario
from ..productos.models import Productos
class Pedido(models.Model):
    descripcion =models.TextField()
    pedido_usario=models.IntegerField()
    entrega_almacen=models.IntegerField()
    total_pedido=models.IntegerField()
    precio_paquete= models.DecimalField(max_digits=10, decimal_places=2)
    cantidad=models.IntegerField()
    total=models.DecimalField(max_digits=10, decimal_places=2)
    estado_pedido = models.BooleanField(default=False)
    usuario=models.ForeignKey(Usuario , models.CASCADE)
    productos= models.ManyToManyField(Productos, through='DetallePedido')   

class DetallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE)