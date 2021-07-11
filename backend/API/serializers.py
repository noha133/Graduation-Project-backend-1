from rest_framework import serializers
from .models import *


class usertypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['user_type']


class departmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = departments
        fields = '__all__'


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Info
        fields = '__all__'


class ClassNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassName
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
        fields = ['Course_Info', 'coursework', 'final']


# class Report_InfoSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Grade
#         fields = '__all__'


class TeacherClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeacherClasses
        fields = ['Course_Info', 'Class']


class ToDoListStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class ToDoListStudentCompletedSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = ['completed']


class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = departments
        fields = '__all__'


class ToDoListTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDoList
        fields = '__all__'


class AssignClassSerializer(serializers.ModelSerializer):
        class Meta:
            model = TeacherClasses
            fields = ['Course_Info', 'Teacher' ,'Class']


class Class(serializers.ModelSerializer):
    class Meta:
        model = ClassName
        fields = '__all__'