from django.shortcuts import render

from .models import student
from .serializers import StudentSerializer

from rest_framework import viewsets
# Create your views here.

class ViewsetStudent(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    