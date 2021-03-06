# Generated by Django 2.1.2 on 2018-11-05 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('address', models.CharField(default=None, max_length=750, null=True)),
                ('timeOpen', models.CharField(default=None, max_length=500, null=True)),
                ('phone', models.CharField(default=None, max_length=250, null=True)),
                ('webSite', models.CharField(default=None, max_length=500, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='sites')),
            ],
        ),
    ]
