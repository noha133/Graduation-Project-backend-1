# Generated by Django 3.2 on 2021-04-20 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0044_remove_grade_coursework'),
    ]

    operations = [
        migrations.AddField(
            model_name='grade',
            name='coursework',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='grade',
            name='final',
            field=models.FloatField(null=True),
        ),
    ]
