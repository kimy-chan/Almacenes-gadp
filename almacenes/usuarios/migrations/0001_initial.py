# Generated by Django 5.0.3 on 2024-05-20 01:37

import django.contrib.auth.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('persona', '0005_alter_persona_cedula_identidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area_trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_area', models.CharField(max_length=100, unique=True)),
                ('rol', models.CharField(blank=True, choices=[('Administrador', 'Administrador'), ('Super_administrador', 'Super administrador'), ('Personal', 'Personal')], default='Personal', null=True, verbose_name='Permisos de rol ')),
            ],
        ),
        migrations.CreateModel(
            name='Secretaria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secretaria', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='Usuario')),
                ('password', models.CharField(max_length=128, verbose_name='Contraseña')),
                ('email', models.EmailField(blank=True, max_length=255, null=True)),
                ('item', models.CharField(blank=True, max_length=100, null=True)),
                ('is_staff', models.CharField(default=True)),
                ('encargado_secretaria', models.CharField(choices=[('Encargado', 'Encargado'), ('Personal', 'Personal')], default='Personal', verbose_name='Jefe  de la secretaria')),
                ('encargado_unidad', models.CharField(choices=[('Encargado', 'Encargado'), ('Personal', 'Personal')], default='Personal', verbose_name='Jefe de la unidad')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persona.persona')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('area_trabajo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.area_trabajo')),
                ('secretaria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.secretaria')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
