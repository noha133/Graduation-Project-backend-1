# Generated by Django 3.1.6 on 2021-04-24 15:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0063_grade_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='user',
        ),
        migrations.AddField(
            model_name='grade',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
