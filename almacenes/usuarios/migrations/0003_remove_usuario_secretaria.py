# Generated by Django 5.0.3 on 2024-07-31 02:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_usuario_area_remove_oficinas_area_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='secretaria',
        ),
    ]
