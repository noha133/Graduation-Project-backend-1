# Generated by Django 3.1.6 on 2021-04-21 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0047_auto_20210421_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='teacherclasses',
            name='Text',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='API.todolist'),
        ),
    ]
