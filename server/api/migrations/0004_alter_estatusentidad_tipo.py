# Generated by Django 4.1.3 on 2022-11-22 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_remove_proyecto_activo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estatusentidad',
            name='tipo',
            field=models.CharField(choices=[('ON', 'Activo'), ('OFF', 'Inactivo')], default='Inactivo', max_length=10),
        ),
    ]
