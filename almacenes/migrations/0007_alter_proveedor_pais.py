# Generated by Django 5.0.3 on 2024-04-14 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('almacenes', '0006_rename_cedulaidentidad_persona_cedula_identidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proveedor',
            name='pais',
            field=models.CharField(max_length=100),
        ),
    ]
