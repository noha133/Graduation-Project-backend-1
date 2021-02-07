from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
  USER_TYPE_CHOICES = (
      (1, 'student'),
      (2, 'teacher'),
      (3, 'supervisor'),
  )
  user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES,default=2)

  def __str__(self):
      return self.username



class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    grade = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Teacher_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.user

class Supervisor_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username



