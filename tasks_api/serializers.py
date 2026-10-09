from rest_framework import serializers
from .models import Task, Comment

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'created_by', 'priority', 'status', 'assigned_to', 'created_at', 'updated_at']

class CommentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Comment
        fields = ['task', 'user', 'content', 'created_at', 'updated_at']