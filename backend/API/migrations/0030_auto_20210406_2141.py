# Generated by Django 3.1.6 on 2021-04-06 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0029_auto_20210406_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_info',
            name='TodoList',
            field=models.CharField(max_length=200, null=True),
        ),
    ]