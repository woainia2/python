from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from .models import Student
from students.serializers import StudentSerializer

class StudentAPIView(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer