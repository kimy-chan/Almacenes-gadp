from django.db import models
from  ..usuarios.models import Usuario
from ..materiales.models import Materiales
class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES=[
        ('Pendiente','Pendiente'),
        ('Incompleto','Incompleto'),
        ('Completo','Completo')
    ]

    ESTADO_AUTORIZACION=[
        (True,'Autorizado'),
        (False,'No autorizado'),
    ]
    descripcion =models.TextField(blank=False , null=False)
    unidad_manejo=models.CharField(max_length=20, blank= False ,null= False)
    cantidad_pedido=models.IntegerField(blank=False, null=False, default=0)
    cantidad_entrega_almacen=models.IntegerField(blank= True ,null= True, default=0)
    partida_presupuestada=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    estado_autorizacion = models.BooleanField(choices=ESTADO_AUTORIZACION, blank=False, null=False, default=False)
    estado_pedido = models.CharField(choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')
    usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE , blank= False, name=False)
    material= models.ForeignKey(Materiales, on_delete=models.CASCADE,  blank= False, name=False)
    fecha_pedido= models.DateTimeField(auto_now_add=True, blank=False, null=False)
    fecha_entrega= models.DateTimeField(blank=True, null=True)
    def __str__(self) -> str:
        return f"Descripción: {self.descripcion}, Unidad de manejo: {self.unidad_manejo}, Cantidad pedido: {self.cantidad_pedido}, Cantidad entrega almacen: {self.cantidad_entrega_almacen}, Partida presupuestada: {self.partida_presupuestada}, Estado de autorización: {self.estado_autorizacion}, Estado del pedido: {self.estado_pedido}, Usuario: {self.usuario}, Producto: {self.material}, Fecha de pedido: {self.fecha_pedido}"
    def fecha_entrega_pedido(self):
        self.fecha_entrega_pedido= self.fecha_entrega_pedido(auto_now_add=True)
        self.save()

