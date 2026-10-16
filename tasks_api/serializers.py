from rest_framework import serializers
from .models import Task, Comment

class UpdateTaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['status']

class TaskSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        assigned_to = validated_data.pop('assigned_to', []) # YOu should separate m2m fields and set it after the object is created
        task = Task.objects.create(created_by=self.context['request'].user, **validated_data) # DRF authomatically inclued current user id in self.context
        task.assigned_to.set(assigned_to)
        return task
    
    class Meta:
        model = Task
        fields = ['title', 'description', 'deadline', 'priority', 'status', 'assigned_to', 'created_at', 'updated_at']


class UpdateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content']

class CommentSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        return Comment.objects.create(user=self.context['request'].user, task_id=self.context['task_id'], **validated_data)

    class Meta: 
        model = Comment
        fields = ['content', 'created_at', 'updated_at']