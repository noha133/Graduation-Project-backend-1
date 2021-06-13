# Generated by Django 3.1.6 on 2021-04-25 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0070_auto_20210425_1249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supervisor_info',
            name='name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teacher_info',
            name='name',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]