from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Info
        fields = ('user','grade')

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher_Info
        fields = ('user','subject')