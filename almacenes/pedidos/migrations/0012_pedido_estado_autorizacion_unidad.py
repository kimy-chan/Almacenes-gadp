# Generated by Django 5.0.3 on 2024-05-30 04:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pedidos', '0011_remove_pedido_estado_autorizacion_unidad'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='estado_autorizacion_unidad',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
    ]