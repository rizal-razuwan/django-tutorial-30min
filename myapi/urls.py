from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.ViewsetStudent)
router.register(r'todo', views.ViewsetTodo)

urlpatterns = [
    path('', include(router.urls)), #no Apostrophe
]
