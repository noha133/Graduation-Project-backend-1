# Generated by Django 3.2 on 2021-04-20 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0042_remove_grade_finalmark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='coursework',
            field=models.FloatField(),
        ),
    ]