from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.http import HttpResponse

    # , permission_classes
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework.decorators import api_view
from django.dispatch import receiver
from django.db.models.signals import post_save


class StudentView(APIView):
    def get_object(self, pk):
            return Student_Info.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        serializer = StudentSerializer(student)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        serializer = StudentSerializer(student, data=request.data)
        courses = Course_Info.objects.filter(semester=student.semester_number)
        for course in courses:
            new_grade = Grade.objects.create(user=student.user, Course_Info=course)
            new_grade.save()
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = student.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)


class TeacherView(APIView):
        # permission_classes = (IsAuthenticated,)
        def get_object(self, pk):
            return Teacher_Info.objects.get(pk=pk)

        def get(self, request, pk, format=None):
            try:
                teacher = self.get_object(pk)
            except Teacher_Info.DoesNotExist:
                return Response("Sorry! Doesn't Exist🙁")

            serializer = TeacherSerializer(teacher)
            return Response(serializer.data)


        def put(self, request, pk, format=None):
            try:
                teacher = self.get_object(pk=pk)
            except Student_Info.DoesNotExist:
                return Response("Sorry! Doesn't Exist🙁")

            serializer = StudentSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        def delete(self, request, pk, format=None):
            try:
                teacher = self.get_object(pk=pk)
            except Teacher_Info.DoesNotExist:
                return Response("Sorry! Doesn't Exist🙁")
            operation = teacher.delete()
            data = {}
            if operation:
                data["sucess"] = "Deleted successfully😘"
            else:
                data["failure"] = "Delete failed😢"
            return Response(data=data)


class SupervisorView(APIView):
    def get_object(self, pk):
        return Supervisor_Info.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        try:
            supervisor = self.get_object(pk=pk)
        except Supervisor_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")

        serializer = Supervisor_InfoSerializer(supervisor)
        return Response(serializer.data)


    def put(self, request, pk, format=None):
        try:
            supervisor = self.get_object(pk=pk)
        except Supervisor_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")

        serializer = Supervisor_InfoSerializer(supervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            supervisor = self.get_object(pk)
        except Supervisor_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = supervisor.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)


class StudentCourseView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")

        courses = Course_Info.objects.filter( semester = student.semester_number.number )
        serializer = Course_InfoSerializer2(courses, many=True)
        return Response(serializer.data)


class GradeView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get_grade(self, pk):
        grade = Grade.objects.get(pk=pk)
        return grade

    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        grades = Grade.objects.filter(user=student.user)
        serializer = Grades_InfoSerializer(grades, many=True)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            grade = self.get_grade(pk=pk)
        except Grade.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        # courses = Course_Info.objects.filter(semester=student.semester_number.number)
        # grades = Grade.objects.filter()
        serializer = Grades_InfoSerializer(grade, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        try:
            grade = self.get_grade(pk = pk)
        except Grade.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = grade.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)


class TeacherCourseView(APIView):
    def get_object(self, pk):
        teacher = Teacher_Info.objects.get(pk=pk)
        return teacher

    def get(self, request, pk, format=None):
        try:
            teacher = self.get_object(pk)
        except Teacher_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        courses = TeacherClasses.objects.filter(Teacher=teacher)
        serializer = AssignClassSerializer(courses, many=True)
        return Response(serializer.data)

class SupervisorClassesView(APIView):
    def get_object(self, pk):
        supervisor = Supervisor_Info.objects.get(pk=pk)
        return supervisor

    def get(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        teachers = Teacher_Info.objects.filter( department=supervisor.department)
        courses = Course_Info.objects.filter(departments=supervisor.department)
        classes = ClassName.objects.all()
        serializer1 = TeacherSerializer(teachers, many=True)
        serializer2 = Course_InfoSerializer(courses, many=True)
        serializer3 = Class(classes, many=True)
        Serializer_list = [serializer1.data, serializer2.data, serializer3.data]
        return Response(Serializer_list)


class AssignClassView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        supervisor = Supervisor_Info.objects.get(pk=pk)
        return supervisor

    def get_assignedclass(self, pk):
        assignedclass = TeacherClasses.objects.get(pk=pk)
        return assignedclass

    def get(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        teachers = Teacher_Info.objects.filter( department=supervisor.department)
        classes = TeacherClasses.objects.filter(Teacher__in=teachers)
        serializer = AssignClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        # supervisor = Supervisor_Info.objects.get(user=request.user)
        # teacherclasses = TeacherClasses(Supervisor=supervisor)
        # serializer = AssignClassSerializer(teacherclasses,data=request.data)
        serializer = AssignClassSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

    def put(self, request, pk, format=None):
        assignedclass = self.get_assignedclass(pk)
        serializer = AssignClassSerializer(assignedclass, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def delete(self, request, pk, format=None):
        try:
            assignedclass = self.get_assignedclass(pk)
        except Supervisor_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = assignedclass.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)

class ToDoListTeacherView(APIView):
    def get_object(self, pk):
        teacher = Teacher_Info.objects.get(pk=pk)
        return teacher

    def get_task(self, pk):
        task = ToDoList.objects.get(pk=pk)
        return task

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        Class = TeacherClasses.objects.filter( Teacher = teacher )
        ToDoLists = ToDoList.objects.filter(TeacherClass__in=Class)
        serializer1 = TeacherClassesSerializer(Class, many=True)
        serializer2 = ToDoListTeacherSerializer(ToDoLists, many=True)
        Serializer_list = [serializer1.data, serializer2.data]
        return Response(Serializer_list)

    def post(self, request, format=None):
        serializer = ToDoListTeacherSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def put(self, request, pk, format=None):
        task = self.get_task(pk)
        serializer = ToDoListTeacherSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            task = self.get_task(pk=pk)
        except ToDoList.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = task.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)


class ToDoListStudentView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        courses = Course_Info.objects.filter(semester=student.semester_number.number)
        Class = TeacherClasses.objects.filter(Class=student.Class, Course_Info__in=courses)
        ToDoLists = ToDoList.objects.filter(TeacherClass__in=Class)
        serializer1 = TeacherClassesSerializer(Class, many=True)
        serializer2 = ToDoListStudentSerializer(ToDoLists, many=True)
        Serializer_list = [serializer1.data, serializer2.data]
        return Response(Serializer_list)


class AnnouncementView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        courses = Course_Info.objects.filter(semester=student.semester_number.number)
        Class = TeacherClasses.objects.filter(Class=student.Class, Course_Info__in=courses)
        ToDoLists = ToDoList.objects.filter(TeacherClass__in=Class,announce=True )
        # task = TeacherClasses.objects.filter(ToDoLists.TeacherClass)
        # serializer1 = TeacherClassesSerializer(Class, many=True)
        serializer2 = ToDoListStudentSerializer(ToDoLists, many=True)
        # Serializer_list = [serializer1.data, serializer2.data]
        # return Response(Serializer_list)
        return Response(serializer2.data)


# class ProgressView(APIView):
#     def get_object(self, pk):
#         supervisor = Supervisor_Info.objects.get(pk=pk)
#         return supervisor
#
#     def get(self, request, pk, format=None):
#         supervisor = self.get_object(pk)
#         courses = Course_Info.objects.filter(departments=supervisor.department)
#         # students = Student_Info.objects.filter( semester_number=courses.semester)
#         # grades = Grade.objects.filter(Student=students)
#         # serializer = Grades_InfoSerializer(grades, many=True)
#         serializer = Course_InfoSerializer(courses, many=True)
#         return Response(serializer.data)


# class StudentView(viewsets.ModelViewSet):
#     queryset = Student_Info.objects.all()
#     serializer_class = StudentSerializer
#
# class TeacherView(viewsets.ModelViewSet):
#     queryset = Teacher_Info.objects.all()
#     serializer_class = TeacherSerializer

