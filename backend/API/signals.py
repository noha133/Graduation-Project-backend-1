from django.db.models import signals
from django.dispatch import receiver
from django.dispatch import dispatcher
from .models import *
from django.db.models.signals import post_save

@receiver(post_save, sender=User)
def user_created(sender, instance, created, **kwargs):
    if created:
        user_type = instance.user_type
        if user_type == "1":
            new_student = Student_Info(user=instance)
                                                # semester = "7"
                                                # courses = Course_Info.objects.filter(semester=semester)
            new_student.save()
                                                 # for course in courses:
                                                 #     new_grade= Grade.objects.create(user = instance,
                                                #     Course_Info = course)
                                                #     new_grade.save()

                                                # new_grade = Grade(user=instance)


                                                 # new_grade.save()

        elif user_type == "2":
            new_teacher = Teacher_Info(user=instance)
            new_teacher.save()
        elif user_type == "3":
            new_supervisor = Supervisor_Info(user=instance)
            new_supervisor.save()

post_save.connect(user_created,sender=User)






# @receiver(post_save, sender=Student_Info)
# def grade_created(sender, instance, created, **kwargs):
#     if created:
#             # semester = Student_Info.semester_number
#         courses = Course_Info.objects.filter(semester=instance.semester_number)
#         for course in courses:
#             new_grade= Grade.objects.create(user = instance.user, Course_Info = course)
#             new_grade.save()
#
# post_save.connect(grade_created,sender=Student_Info.name)

