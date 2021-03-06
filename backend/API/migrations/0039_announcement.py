# Generated by Django 3.2 on 2021-04-19 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0038_auto_20210419_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
                ('display', models.BooleanField(default=False)),
                ('level', models.CharField(choices=[('warning', 'Warning'), ('error', 'Error'), ('success', 'Success'), ('info', 'Info')], default='info', max_length=7)),
            ],
        ),
    ]
