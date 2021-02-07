# Generated by Django 3.1.6 on 2021-02-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20210207_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[('1', 'student'), ('2', 'teacher'), ('3', 'supervisor')], default='2', max_length=10),
        ),
    ]
