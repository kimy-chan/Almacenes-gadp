# Generated by Django 5.0.3 on 2024-05-13 02:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('materiales', '0002_materiales_precio_unidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('unidad_manejo', models.CharField(max_length=20)),
                ('cantidad_pedida', models.IntegerField(default=0)),
                ('cantidad_entrega', models.IntegerField(blank=True, default=0, null=True)),
                ('partida_presupuestada', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('costo_unidad', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('costo_total', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado_autorizacion_unidad', models.BooleanField(blank=True, default=False, null=True)),
                ('estado_autorizacion_unidad_mayor', models.BooleanField(blank=True, default=False, null=True)),
                ('estado_autorizacion_director_administrativo', models.BooleanField(blank=True, default=False, null=True)),
                ('estado_pedido_almacen', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Incompleto', 'Incompleto'), ('Completo', 'Completo')], default='Pendiente')),
                ('programa', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('sub_programa', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('proyecto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('act_u_obra', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('unidad_ejecucion', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('codigo_presupuesto', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('codigo_numero', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('fecha_pedido', models.DateTimeField(auto_now_add=True)),
                ('fecha_entrega_salida', models.DateTimeField(blank=True, null=True)),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.materiales')),
            ],
        ),
    ]
