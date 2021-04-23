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

        serializer1 = StudentSerializer(student, data=request.data)
        if serializer1.is_valid():
            serializer1.save()
            courses = Course_Info.objects.filter(semester=student.semester_number.number)
            Report = Grade.objects.create(Student=student, Course_Info=courses, coursework=0.0, final=0.0)
            serializer2 = Course_InfoSerializer2(courses, many=True)
            serializer3 = Grades_InfoSerializer(Report, many=True)
            serializer3.save()
            Serializer_list = [serializer1.data, serializer2.data, serializer3.data]
            return Response(Serializer_list)

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
    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        grades = Grade.objects.filter(Student=student)
        serializer = Grades_InfoSerializer(grades, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        teacher = Teacher_Info.objects.get(pk=request.user)
        serializer = Grades_InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Grade.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        courses = Course_Info.objects.filter(semester=student.semester_number.number)
        grades = Grade.objects.filter(Student=student, Course_Info__in=courses)
        serializer = Grades_InfoSerializer(grades, data=request.data, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            grades = self.get_object(pk = pk)
        except Grade.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = grades.delete()
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
        teacher = self.get_object(pk)
        courses = TeacherClasses.objects.filter( Teacher = teacher )
        serializer = TeacherClassesSerializer(courses, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = TeacherClassesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        teacher = self.get_object(pk)
        courses = TeacherClasses.objects.filter(Teacher=teacher)
        serializer = TeacherClassesSerializer(courses, data=request.data)
        # serializer = TeacherClassesSerializer(courses, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):

        courses = self.get_object(pk)
        courses.delete()


class ToDoListTeacherView(APIView):
    def get_object(self, pk):
        teacher = Teacher_Info.objects.get(pk=pk)
        return teacher

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

    def put(self, request, pk, format=None):
        todolist = self.get_object(pk)
        serializer = ToDoListTeacherSerializer(todolist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        todolist = self.get_object(pk)
        todolist.delete()


class ToDoListStudentView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
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
        student = self.get_object(pk)
        courses = Course_Info.objects.filter(semester=student.semester_number.number)
        Class = TeacherClasses.objects.filter(Class=student.Class, Course_Info__in=courses)
        ToDoLists = ToDoList.objects.filter(TeacherClass__in=Class,announce=True )
        # task = TeacherClasses.objects.filter(ToDoLists.TeacherClass)
        serializer1 = TeacherClassesSerializer(Class, many=True)
        serializer2 = ToDoListStudentSerializer(ToDoLists, many=True)
        Serializer_list = [serializer1.data, serializer2.data]
        return Response(Serializer_list)


class AssignClassView(APIView):
    # permission_classes = (IsAuthenticated,)
    def get_object(self, pk):
        supervisor = Supervisor_Info.objects.get(pk=pk)
        return supervisor

    def get(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        teachers = Teacher_Info.objects.filter( department=supervisor.department)
        classes = TeacherClasses.objects.filter(Teacher__in=teachers)
        serializer = AssignClassSerializer(classes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        account = request.user
        # supervisor = Supervisor_Info(user=account)
        teacherclasses = TeacherClasses(Supervisor=account)
        # teachers = Teacher_Info.objects.filter(department=supervisor.department)
        # courses = Course_Info.objects.filter(department=supervisor.department)
        # classes = ClassName.objects.all()
        serializer = AssignClassSerializer(teacherclasses,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        serializer = AssignClassSerializer(supervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        try:
            supervisor = self.get_object(pk=pk)
        except Supervisor_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        operation = supervisor.delete()
        data = {}
        if operation:
            data["sucess"] = "Deleted successfully😘"
        else:
            data["failure"] = "Delete failed😢"
        return Response(data=data)


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


# @api_view(['GET', 'PUT', 'DELETE'])
# def test_view(request, pk):
#
#     qs = Teacher_Info.objects.all()/
#     qs_ser


    # if request.method == 'GET':
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)
class   ReportView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student
    def get(self, request, pk, format=None):
        try:
            student = self.get_object(pk=pk)
        except Student_Info.DoesNotExist:
            return Response("Sorry! Doesn't Exist🙁")
        courses = Course_Info.objects.filter(semester=student.semester_number.number)
        grade = Grade.objects.filter(Course_Info__in=courses)
        report =Grade.objects.filter(Student=student, grades__in=grade)
        serializer = Report_InfoSerializer(report, many=True)
        return Response(serializer.data)