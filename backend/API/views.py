from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework.decorators import api_view


class StudentView(APIView):
    # permission_classes = (IsAuthenticated, )

    # def get(request,pk):
    #     qs = Student_Info.objects.get(pk=pk)
    #     students = StudentSerializer(qs , many=True)
    #     # qs = Course_Info.objects.name(Student_Info.objects.semester)
    #     # Courses = Course_InfoSerializer(qs,many=True)
    #     return Response(students.data)

    # def post(self, request, *args, **kwargs):
    #     qs = Student_Info.objects.all()
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #
    #     return Response(serializer.data)
    def get_object(self, pk):
            return Student_Info.objects.get(pk=pk)
    # def get_course(self, pk):
    #         return Course_Info.name.get(pk=Student_Info.Semester_Info)

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student)
        # courses = self.get_course(pk)
        # serializer += Course_InfoSerializer(courses)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


    def delete(self, request, pk, format=None):
        student = self.get_object(pk)
        student.delete()

class TeacherView(APIView):
        def get_object(self, pk):
            return Teacher_Info.objects.get(pk=pk)

        def get(self, request, pk, format=None):
            teacher = self.get_object(pk)
            serializer = TeacherSerializer(teacher)
            # courses = self.get_course(pk)
            # serializer += Course_InfoSerializer(courses)
            return Response(serializer.data)

        def post(self, request, format=None):
            serializer = TeacherSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        def put(self, request, pk, format=None):
            teacher = self.get_object(pk)
            serializer = StudentSerializer(teacher, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)

        def delete(self, request, pk, format=None):
            teacher = self.get_object(pk)
            teacher.delete()


class SupervisorView(APIView):
    def get_object(self, pk):
        return Supervisor_Info.objects.get(pk=pk)

    def get(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        serializer = Supervisor_InfoSerializer(supervisor)
        # courses = self.get_course(pk)
        # serializer += Course_InfoSerializer(courses)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = Supervisor_InfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def put(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        serializer = Supervisor_InfoSerializer(supervisor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, request, pk, format=None):
        supervisor = self.get_object(pk)
        supervisor.delete()



class CourseView(APIView):
    def get_object(self, pk):
        student = Student_Info.objects.get(pk=pk)
        return student

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        courses = Course_Info.objects.filter( semester = student.semester_number.number )
        serializer = Course_InfoSerializer2(courses, many=True)
        return Response(serializer.data)

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
