# Generated by Django 3.1.6 on 2021-04-02 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0007_auto_20210401_2246'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_info',
            name='semester',
            field=models.CharField(default=None, max_length=100),
            preserve_default=False,
        ),
    ]
