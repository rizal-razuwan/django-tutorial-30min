from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=250)
    course = models.CharField(max_length=250)
    age = models.CharField(max_length=10)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title
        