# Generated by Django 4.0.4 on 2022-06-29 23:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producto', '0005_direccion_alter_producto_nombre_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='serieCliente',
        ),
    ]