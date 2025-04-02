# views.py
from django.shortcuts import render
from rest_framework import viewsets  # Added missing import
from .models import Task
from .serializers import TaskSerializer  # Fixed import name
# Create your views here.
class TaskViewset(viewsets.ModelViewSet):  # Make sure this matches the name in urls.py
    queryset = Task.objects.all()
    serializer_class = TaskSerializer  # Fixed class name