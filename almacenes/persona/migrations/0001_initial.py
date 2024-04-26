# Generated by Django 5.0.3 on 2024-04-24 02:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creation', models.DateTimeField(auto_now_add=True)),
                ('cedula_identidad', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=50)),
                ('apellidos', models.CharField(max_length=60)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
