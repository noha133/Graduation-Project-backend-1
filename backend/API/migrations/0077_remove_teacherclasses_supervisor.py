# Generated by Django 3.1.6 on 2021-04-25 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0076_auto_20210425_1401'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherclasses',
            name='Supervisor',
        ),
    ]