# Generated by Django 5.0.3 on 2024-05-08 02:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_clasificacion', models.CharField(error_messages={'unique': 'El codigo de la categoria ya existe'}, max_length=100, unique=True)),
                ('nombre', models.CharField(error_messages={'unique': 'El nombre de la categoria ya existe'}, max_length=200, unique=True)),
                ('fecha_creacion', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Materiales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('codigo', models.CharField(error_messages={'unique': 'El codigo de producto ya existe'}, max_length=255, unique=True)),
                ('marca', models.CharField(max_length=255)),
                ('cantidad_paquete', models.IntegerField(verbose_name='Cantidad por paquetes')),
                ('cantidad_paquete_unidad', models.IntegerField(verbose_name='Cantidad por paquetes (en unidades)')),
                ('stock', models.IntegerField(null=True)),
                ('precio_paquete', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Precio por paquetes')),
                ('total_precio', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('tamaño', models.CharField(blank=True, max_length=255, null=True)),
                ('color', models.CharField(blank=True, max_length=100, null=True)),
                ('unidad_medida', models.CharField(blank=True, max_length=255, null=True, verbose_name='Unidad de medida')),
                ('material', models.CharField(blank=True, max_length=255, null=True)),
                ('numero_serie', models.CharField(blank=True, error_messages={'unique': 'El numero de serie de producto ya existe'}, max_length=255, null=True, unique=True, verbose_name='Numero de serie')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='materiales.categoria')),
            ],
        ),
    ]