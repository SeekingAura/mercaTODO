# Generated by Django 2.1.2 on 2018-11-17 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20181117_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='unit',
            field=models.CharField(choices=[('Unidad', 'Unidad'), ('Gramo', 'Gramo'), ('Libra', 'Libra'), ('Kilogramo', 'Kilogramo')], default='Unidad', max_length=20, verbose_name='Unidad de venta'),
        ),
        migrations.AlterField(
            model_name='siteproduct',
            name='lastUpdate',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
