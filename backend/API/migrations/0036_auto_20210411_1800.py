# Generated by Django 3.2 on 2021-04-11 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0035_auto_20210410_2214'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherclasses',
            name='Text',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.DeleteModel(
            name='ToDoList',
        ),
    ]