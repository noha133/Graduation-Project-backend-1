from django.db.models.signals import post_save
from django.contrib.auth.models import Group

from .models import *

def user_created(sender, instance, created, **kwargs):
    if created:
        user_type = instance.user_type
        if user_type == 1:
            new_student = Student_Info(user = instance)
        elif user_type == 2 :
            new_teacher = Teacher_Info(user = instance)
        elif user_type == 3:
            new_supervisor = Supervisor_Info(user=instance)


post_save.connect(user_created, sender=User)