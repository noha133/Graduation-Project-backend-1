from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      ("1", 'student'),
      ("2", 'teacher'),
      ("3", 'supervisor'),
  )
  user_type = models.CharField(choices=USER_TYPE_CHOICES,default="2",null=False , max_length=10)

  def __str__(self):
      return self.username



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
    TodoList = models.CharField(max_length=200, null=True)
    def __str__(self):
        return str(self.name)


class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    semester_number = models.ForeignKey(Semester_Info, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.user)


class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    Course_Info = models.ManyToManyField(Course_Info)
    departments = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user)


class Supervisor_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=100)
    departments = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.user)

class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    Student = models.ForeignKey(Student_Info, null=True, on_delete=models.SET_NULL)
    Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.number)