from django.shortcuts import render
from rest_framework import generics
from .models import Task
from .serializers import TaskSerializer

# Create your views here.
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
