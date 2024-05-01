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
    cantidad_entrega_almacen=models.IntegerField(blank= True ,null= True)
    partida_presupuestada=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    estado_autorizacion = models.CharField(choices=ESTADO_AUTORIZACION, default='No autorizado')
    estado_pedido = models.CharField(choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')
    usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE , blank= False, name=False)
    producto= models.ForeignKey(Productos, on_delete=models.CASCADE,  blank= False, name=False)
    fecha_pedido= models.DateTimeField(auto_now_add=True, blank=False, null=False)

    def __str__(self) -> str:
        return f"Descripción: {self.descripcion}, Unidad de manejo: {self.unidad_manejo}, Cantidad pedido: {self.cantidad_pedido}, Cantidad entrega almacen: {self.cantidad_entrega_almacen}, Partida presupuestada: {self.partida_presupuestada}, Estado de autorización: {self.estado_autorizacion}, Estado del pedido: {self.estado_pedido}, Usuario: {self.usuario}, Producto: {self.producto}, Fecha de pedido: {self.fecha_pedido}"
