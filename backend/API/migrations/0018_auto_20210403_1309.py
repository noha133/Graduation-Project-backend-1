# Generated by Django 3.1.6 on 2021-04-03 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0017_auto_20210403_0116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student_info',
            name='semester',
        ),
        migrations.AlterField(
            model_name='course_info',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
