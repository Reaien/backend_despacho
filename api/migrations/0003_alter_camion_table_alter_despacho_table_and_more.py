# Generated by Django 5.0.6 on 2024-05-10 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_camion_remove_despacho_camion_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='camion',
            table='Camion',
        ),
        migrations.AlterModelTable(
            name='despacho',
            table='Despacho',
        ),
        migrations.AlterModelTable(
            name='resumen_despacho',
            table='Resumen_Despacho',
        ),
    ]
