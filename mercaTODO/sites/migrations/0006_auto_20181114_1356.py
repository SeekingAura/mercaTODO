# Generated by Django 2.1.2 on 2018-11-14 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0005_auto_20181114_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='User',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
