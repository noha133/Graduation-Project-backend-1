from rest_framework import serializers
from .models import Student,Teacher

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('username','password')

