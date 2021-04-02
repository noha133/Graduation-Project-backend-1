from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *
from rest_framework import mixins




class TestView(APIView):
    # permission_classes = (IsAuthenticated, )

    def get(self, request, *args, **kwargs):
        qs = Student_Info.objects.all()
        post = qs.first()
        # serializer = PostSerializer(qs, many=True)
        serializer = StudentSerializer(post)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)

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