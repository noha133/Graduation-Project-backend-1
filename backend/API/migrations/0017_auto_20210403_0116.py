# Generated by Django 3.1.6 on 2021-04-02 23:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0016_remove_course_info_semester'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course_info',
            name='Student_Info',
        ),
        migrations.RemoveField(
            model_name='course_info',
            name='Supervisor_Info',
        ),
        migrations.RemoveField(
            model_name='course_info',
            name='Teacher_Info',
        ),
    ]