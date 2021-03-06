# Generated by Django 2.1.2 on 2018-11-05 17:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('unit', models.CharField(choices=[('unit', 'Unidad'), ('gram', 'Gramo'), ('pound', 'Libra'), ('kilogram', 'Kilogramo')], default='unit', max_length=20)),
                ('image', models.ImageField(default=None, null=True, upload_to='products')),
            ],
        ),
        migrations.CreateModel(
            name='SiteProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product')),
                ('site', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sites.Site')),
            ],
        ),
    ]
