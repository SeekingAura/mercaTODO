# Generated by Django 2.1.2 on 2018-11-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='products'),
        ),
    ]