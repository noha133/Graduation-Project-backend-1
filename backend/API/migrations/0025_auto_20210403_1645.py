# Generated by Django 3.1.6 on 2021-04-03 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0024_teacher_info_course_info'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student_info',
            old_name='Semester_Info',
            new_name='Courses',
        ),
        migrations.AddField(
            model_name='student_info',
            name='semester_number',
            field=models.IntegerField(default=None, max_length=10),
            preserve_default=False,
        ),
    ]
