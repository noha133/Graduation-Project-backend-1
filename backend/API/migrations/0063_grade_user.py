# Generated by Django 3.1.6 on 2021-04-24 15:05

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0062_auto_20210423_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
