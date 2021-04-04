from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TaskSerializer
from .models import Todo

#Create ToDo viewset
class TodoView(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Todo.objects.all()
