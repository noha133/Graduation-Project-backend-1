# Generated by Django 3.1.6 on 2021-04-21 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0046_teacherclasses_supervisor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacherclasses',
            name='Text',
            field=models.TextField(blank=True),
        ),
    ]
