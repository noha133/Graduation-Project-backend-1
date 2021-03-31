from rest_framework import serializers
from .models import *



class departmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = department
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Info
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Info
        fields = '__all__'



class Supervisor_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supervisor_Info
        fields = '__all__'


class Course_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Info
        fields = '__all__'