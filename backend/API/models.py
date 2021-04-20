from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
  USER_TYPE_CHOICES = (
      ("1", 'student'),
      ("2", 'teacher'),
      ("3", 'supervisor'),
  )
  user_type = models.CharField(choices=USER_TYPE_CHOICES,default="2",null=False , max_length=10)
  def __str__(self):
      return self.username

LEVEL_CHOICES = (
     ('warning', 'Warning'),
     ('error', 'Error'),
     ('success', 'Success'),
     ('info', 'Info'),
)
class Announcement(models.Model):
    body = models.TextField(blank=False)
    display = models.BooleanField(default=False)
    level = models.CharField(max_length=7,
                choices=LEVEL_CHOICES, default='info')
    def __unicode__(self):
        return self.body[:50]


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
    def __str__(self):
        return str(self.name)


class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    semester_number = models.ForeignKey(Semester_Info, null=True, on_delete=models.SET_NULL)
    Class = models.ForeignKey(ClassName, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.user)


class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=100)
    department = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.user)


class Supervisor_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    department = models.ForeignKey(departments, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.user)


class Grade(models.Model):
    id = models.AutoField(primary_key=True)
    number = models.IntegerField()
    Student = models.ForeignKey(Student_Info, null=True, on_delete=models.SET_NULL)
    Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.number)


class TeacherClasses(models.Model):
    Teacher = models.ForeignKey(Teacher_Info, null=True, on_delete=models.SET_NULL)
    Course_Info = models.ForeignKey(Course_Info, null=True, on_delete=models.SET_NULL)
    Class = models.ForeignKey(ClassName, null=True, on_delete=models.SET_NULL)
    Text = models.CharField(max_length=100, null=True)
    def __str__(self):
        return str(self.Course_Info)

