from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from datetime import datetime


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      ("1", 'student'),
      ("2", 'teacher'),
      ("3", 'supervisor'),
  )
  user_type = models.CharField(choices=USER_TYPE_CHOICES, default="2", null=False, max_length=10)
  def __str__(self):
      return self.username


class ClassName(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)


class departments(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return str(self.name)


class Semester_Info(models.Model):
    number = models.IntegerField(primary_key=True)
    def __str__(self):
        return str(self.number)


class Course_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    departments = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)
    semester = models.ForeignKey(Semester_Info, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('name', 'departments',)

    def __str__(self):
        return str(self.name)


class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    semester_number = models.ForeignKey(Semester_Info, null=True, on_delete=models.SET_NULL)
    Class = models.ForeignKey(ClassName, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('user', 'Class',)

    def __str__(self):
        return str(self.user)


class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('user', 'department',)

    def __str__(self):
        return str(self.user)


class Supervisor_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('user', 'department',)

    def __str__(self):
        return str(self.user)


class Grade(models.Model):
    user =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    id = models.AutoField(primary_key=True)
    Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    coursework = models.FloatField( null=True)
    final = models.FloatField(null=True)

    class Meta:
        unique_together = ('user', 'Course_Info',)

    def __str__(self):
        return str(self.user)
        # return f'{self.Student} {self.Course_Info} {self.coursework + self.final}'

class TeacherClasses(models.Model):
    Teacher = models.ForeignKey(Teacher_Info, null=True, on_delete=models.SET_NULL)
    Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    Class = models.ForeignKey(ClassName, null=True, on_delete=models.SET_NULL)

    class Meta:
        unique_together = ('Course_Info', 'Class',)

    def __str__(self):
        return f'{self.Course_Info} {self.Class} {self.Teacher}'


TASK_CHOICES = (
     ('homework', 'HomeWork'),
     ('reminder', 'Reminder'),
     ('quiz', 'Quiz'),
)

class ToDoList(models.Model):
    TeacherClass = models.ForeignKey(TeacherClasses, null=True, on_delete=models.SET_NULL)
    body = models.TextField(blank=True)
    link = models.CharField(max_length=360, null=True,blank=True)
    type = models.CharField(max_length=8, choices=TASK_CHOICES, default='homework')
    completed = models.BooleanField(default=False)
    announce = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True, blank=True)
    deadline = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.TeacherClass)
