# Generated by Django 3.1.6 on 2021-04-25 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0065_auto_20210425_0055'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='flag',
            field=models.IntegerField(null=True),
        ),
    ]
