from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'student', views.ViewsetStudent)

urlpatterns = [
    path('', include(router.urls)), #no Apostrophe
]
