from django.shortcuts import render
from rest_framework.permissions import IsAdminUser, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Task, Comment
from .serializers import TaskSerializer, UpdateTaskSerializer, CommentSerializer, UpdateCommentSerializer
from .permissions import IsCommentCreatorOrAdmin, IsTaskCreatorOrAdmin, IsTaskCreator



class TaskViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']
    
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsTaskCreatorOrAdmin()]
        return [IsAuthenticated()]

class TaskStatusViewSet(ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = UpdateTaskSerializer
    lookup_url_kwarg = 'task_pk'

    def get_permissions(self):
        if self.request.method == 'PATCH':
            return [IsTaskCreator()]
        return [IsAuthenticated()]



class CommentViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']


    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return CommentSerializer
        return UpdateCommentSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['task_id'] = self.kwargs['task_pk']
        return context

    def get_queryset(self):
        return Comment.objects.filter(task_id=self.kwargs['task_pk'])

    def get_permissions(self):
        if self.request.method in ['PUT', 'DELETE']:
            return [IsCommentCreatorOrAdmin()]
        return [IsAuthenticated()]

