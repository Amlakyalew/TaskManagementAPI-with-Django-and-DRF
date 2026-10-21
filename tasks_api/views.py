from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.db.models import Q

from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated, SAFE_METHODS
from rest_framework.viewsets import ModelViewSet
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.response import Response


from .models import Task, Comment
from .serializers import TaskSerializer, UpdateTaskSerializer, CommentSerializer, UpdateCommentSerializer, RegisterSerializer
from .permissions import IsCommentCreatorOrAdmin, IsTaskCreatorOrAdmin, IsTaskCreator



class TaskViewSet(ModelViewSet):
    http_method_names = ['get', 'post', 'put', 'delete', 'head', 'options']
    
    serializer_class = TaskSerializer

    def get_queryset(self):
        context = super().get_serializer_context()
        return Task.objects.filter(Q(assigned_to=self.request.user) | Q(created_by=self.request.user))
    

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
        if self.request.method == 'POST':
            return UpdateCommentSerializer
        return CommentSerializer

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


User = get_user_model()

class RegisterViewSet(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def get_permissions(self):
        if self.action == 'me':
            return [IsAuthenticated()]
        return [IsAdminUser()]

    @action(detail=False, methods=['GET', 'PATCH'])
    def me(self, request):
        if request.method == 'PATCH':
            serializer = self.get_serializer(request.user, request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        serializer = self.get_serializer(request.user)
        return Response(serializer.data)