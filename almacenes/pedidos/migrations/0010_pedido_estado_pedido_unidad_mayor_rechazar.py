# Generated by Django 5.0.3 on 2024-05-30 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0009_remove_pedido_estado_pedido_unidad_mayor_rechazar'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado_pedido_unidad_mayor_rechazar',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]