# Generated by Django 5.0.3 on 2024-05-23 02:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_usuario_es_habilitado_alter_area_trabajo_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='es_activo',
            field=models.BooleanField(default=True),
        ),
    ]
