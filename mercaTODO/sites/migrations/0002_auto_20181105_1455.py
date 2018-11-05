# Generated by Django 2.1.2 on 2018-11-05 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='address',
            field=models.CharField(blank=True, default=None, max_length=750, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='sites'),
        ),
        migrations.AlterField(
            model_name='site',
            name='phone',
            field=models.CharField(blank=True, default=None, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='timeOpen',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='site',
            name='webSite',
            field=models.CharField(blank=True, default=None, max_length=500, null=True),
        ),
    ]