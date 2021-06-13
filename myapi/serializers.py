from django.db import models
from django.db.models import fields
from .models import student, Todo
from rest_framework import serializers

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = '__all__'


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'
