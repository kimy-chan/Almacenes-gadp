# Generated by Django 5.0.3 on 2024-05-22 01:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('materiales', '0004_materiales_es_habilitado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materiales',
            name='stock',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
