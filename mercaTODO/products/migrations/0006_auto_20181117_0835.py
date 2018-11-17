# Generated by Django 2.1.2 on 2018-11-17 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_siteproduct_lastupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteproduct',
            name='status',
            field=models.CharField(choices=[('sin cambios', 'Sin cambios'), ('nuevo', 'Nuevo'), ('modificado', 'Modificado')], default='sin cambios', max_length=20, verbose_name='Estado de almacenamiento'),
        ),
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Unidad', 'Unidad'), ('Gramo', 'Gramo'), ('Libra', 'Libra'), ('Kilogramo', 'Kilogramo')], default='unit', max_length=20, verbose_name='Unidad de venta'),
        ),
    ]
