from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Task, Comment
from .serializers import TaskSerializer, CommentSerializer



class TaskViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
