# Generated by Django 3.1.6 on 2021-04-06 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0032_auto_20210406_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]