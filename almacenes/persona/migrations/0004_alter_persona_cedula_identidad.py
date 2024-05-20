# Generated by Django 5.0.3 on 2024-05-19 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_alter_persona_cedula_identidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='persona',
            name='cedula_identidad',
            field=models.CharField(error_messages={'Ya existe la cedula de identidad registrada'}, max_length=20, unique=True),
        ),
    ]
