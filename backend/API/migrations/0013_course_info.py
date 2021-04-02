# Generated by Django 3.1.6 on 2021-04-02 22:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0012_delete_course_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_Info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('semester', models.CharField(max_length=100)),
                ('Student_Info', models.ManyToManyField(to='API.Student_Info')),
                ('Supervisor_Info', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.supervisor_info')),
                ('Teacher_Info', models.ManyToManyField(to='API.Teacher_Info')),
            ],
        ),
    ]
