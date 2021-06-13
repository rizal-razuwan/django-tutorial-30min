from django.shortcuts import render

from .models import student, Todo
from .serializers import StudentSerializer, TodoSerializer

from rest_framework import viewsets
# Create your views here.

class ViewsetStudent(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer

class ViewsetTodo(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    