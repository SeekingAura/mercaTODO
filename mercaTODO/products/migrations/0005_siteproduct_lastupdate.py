# Generated by Django 2.1.2 on 2018-11-15 23:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20181114_1355'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteproduct',
            name='lastUpdate',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 11, 15, 23, 42, 33, 330755)),
            preserve_default=False,
        ),
    ]
