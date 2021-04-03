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


class Course_Info(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    departments = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)
    #semester = models.CharField(max_length=100,null=False)
    # Student_Info = models.ForeignKey(Student_Info, null=True, on_delete=models.SET_NULL)
    # Student_Info = models.ManyToManyField(Student_Info)
    # Teacher_Info = models.ManyToManyField(Teacher_Info)
    # Teacher_Info = models.ForeignKey(Teacher_Info, null=True, on_delete=models.SET_NULL)
    # Supervisor_Info = models.ForeignKey(Supervisor_Info, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.name)


class Semester_Info(models.Model):
    number = models.IntegerField(primary_key=True)
    # Teacher_Info = models.ManyToManyField(Teacher_Info)
    # Student_Info = models.ForeignKey(Student_Info, null=True, on_delete=models.SET_NULL)
    # Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    Course_Info = models.ManyToManyField(Course_Info)

    # number = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    # subject = models.CharField(max_length=100)
    # departments = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return str(self.number)


class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=100)
    Semester_Info = models.ForeignKey(Semester_Info, null=True, on_delete=models.SET_NULL)
    #semester = models.CharField(max_length=100,null=False)
    #semester = models.CharField(max_length=100,null=False)


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