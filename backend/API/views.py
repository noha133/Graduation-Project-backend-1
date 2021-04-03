from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import mixins
from rest_framework.decorators import api_view


class TestView(APIView):
    # permission_classes = (IsAuthenticated, )

    # def get(request,pk):
    #     qs = Student_Info.objects.get(pk=pk)
    #     students = StudentSerializer(qs , many=True)
    #     # qs = Course_Info.objects.name(Student_Info.objects.semester)
    #     # Courses = Course_InfoSerializer(qs,many=True)
    #     return Response(students.data)

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



    # def post(self, request, *args, **kwargs):
    #     qs = Student_Info.objects.all()
    #     serializer = StudentSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #
    #     return Response(serializer.data)

# class StudentView(viewsets.GenericViewSet,mixins.CreateModelMixin,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,mixins.ListModelMixin,):
#     queryset1 = Student_Info.objects.all()
#     queryset2 = Course_Info.objects.values_list('name')
#     queryset1.union(queryset2).order_by('semester')
#     serializer_class = StudentSerializer.data + Course_InfoSerializer

class StudentView(viewsets.ModelViewSet):
    queryset = Student_Info.objects.all()
    serializer_class = StudentSerializer

class TeacherView(viewsets.ModelViewSet):
    queryset = Teacher_Info.objects.all()
    serializer_class = TeacherSerializer


# @api_view(['GET', 'PUT', 'DELETE'])
# def test_view(request, pk):
#
#     qs = Teacher_Info.objects.all()
#     qs_ser


    # if request.method == 'GET':
    #     serializer = SnippetSerializer(snippet)
    #     return Response(serializer.data)