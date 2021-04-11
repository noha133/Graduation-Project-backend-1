from rest_framework import serializers
from .models import *



class departmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = departments
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

class Course_InfoSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Course_Info
        fields = ['name']

class Semester_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semester_Info
        fields = '__all__'

class Grades_InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grade
        fields = ['Course_Info', 'number']

class TeacherClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasses
        fields = ['Course_Info', 'Class']

class ToDoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasses
        fields = ['Course_Info', 'Class', 'Text']