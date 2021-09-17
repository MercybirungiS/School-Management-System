from events.models import Events
from django.db.models.query import QuerySet
from rest_framework import serializers
from courses.models import Courses
from rest_framework.serializers import Serializer
from trainer.models import Trainer
from django.shortcuts import render
from rest_framework import viewsets
from student.models import Student
from events.models import Events
from .serializers import StudentSerializer,TrainerSerializer,CourseSerializer,EventSerializer

# Create your views here.

class StudentViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class TrainerViewSet(viewsets.ModelViewSet):
    queryset=Trainer.objects.all()
    serializer_class=TrainerSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset=Courses.objects.all()
    serializer_class=CourseSerializer

class EventViewSet(viewsets.ModelViewSet):
    queryset=Events.objects.all()
    serializer_class=EventSerializer



 
