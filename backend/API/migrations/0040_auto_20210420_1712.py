# Generated by Django 3.2 on 2021-04-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0039_announcement'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grade',
            name='number',
        ),
        migrations.AddField(
            model_name='grade',
            name='coursework',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='grade',
            name='final',
            field=models.FloatField(default=None),
            preserve_default=False,
        ),
    ]
