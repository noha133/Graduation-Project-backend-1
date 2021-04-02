from django.db.models import signals
from django.dispatch import receiver
from django.dispatch import dispatcher
from .models import *
from django.db.models.signals import post_save


@receiver(models.signals.post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user_type = instance.user_type
        if user_type == "1":
            new_student = Student_Info(user = instance)
        elif user_type == "2":
            new_teacher = Teacher_Info(user = instance)
        elif user_type == "3":
            new_supervisor = Supervisor_Info(user=instance)


dispatcher.connect(user_created, signal=signals.post_save, sender=User)