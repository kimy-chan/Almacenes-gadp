# Generated by Django 5.0.3 on 2024-05-19 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0002_materiales_precio_unidad'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='materiales',
            name='numero_serie',
        ),
        migrations.AddField(
            model_name='materiales',
            name='codigo_paquete',
            field=models.CharField(blank=True, error_messages={'unique': 'El codigo ya existe'}, max_length=255, null=True, unique=True, verbose_name='Codigo de paquete'),
        ),
    ]
