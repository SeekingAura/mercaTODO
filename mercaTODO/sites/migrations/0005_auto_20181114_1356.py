# Generated by Django 2.1.2 on 2018-11-14 18:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0004_site_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='site',
            name='User',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
