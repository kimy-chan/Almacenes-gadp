from django.db import models
from  ..usuarios.models import Usuario
from ..materiales.models import Materiales
class Pedido(models.Model):
    ESTADO_PEDIDO_CHOICES=[
        ('Pendiente','Pendiente'),
        ('Incompleto','Incompleto'),
        ('Completo','Completo')
    ]

    descripcion =models.TextField(blank=False , null=False)
    unidad_manejo=models.CharField(max_length=20, blank= False ,null= False)
    cantidad_pedida=models.IntegerField(blank=False, null=False, default=0)
    cantidad_entrega=models.IntegerField(blank= True ,null= True, default=0)
    partida_presupuestada=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    costo_unidad=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    costo_total=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    estado_autorizacion_unidad = models.BooleanField( blank=True, null=True, default=False)
    estado_autorizacion_unidad_mayor = models.BooleanField( blank=True, null=True, default=False)
    estado_autorizacion_director_administrativo = models.BooleanField( blank=True, null=True, default=False)
    estado_pedido_almacen = models.CharField(choices=ESTADO_PEDIDO_CHOICES, default='Pendiente')
    programa= models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    sub_programa=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    proyecto=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    act_u_obra=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    unidad_ejecucion=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    codigo_presupuesto=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    codigo_numero=models.DecimalField(max_digits=10, decimal_places=2,blank= True ,null= True)
    usuario=models.ForeignKey(Usuario , on_delete=models.CASCADE , blank= False, null=False)
    material= models.ForeignKey(Materiales, on_delete=models.CASCADE,  blank= False, null=False)
    fecha_pedido= models.DateTimeField(auto_now_add=True, blank=False, null=False)
    fecha_entrega_salida= models.DateTimeField(blank=True, null=True)
    
    def __str__(self) -> str:
        return f"Descripción: {self.descripcion}, Unidad de manejo: {self.unidad_manejo}, Cantidad pedido: {self.cantidad_pedido}, Cantidad entrega almacen: {self.cantidad_entrega_almacen}, Partida presupuestada: {self.partida_presupuestada}, Estado de autorización: {self.estado_autorizacion}, Estado del pedido: {self.estado_pedido}, Usuario: {self.usuario}, Producto: {self.material}, Fecha de pedido: {self.fecha_pedido}"
    def fecha_entrega_pedido(self):
        self.fecha_entrega_pedido= self.fecha_entrega_pedido(auto_now_add=True)
        self.save()

