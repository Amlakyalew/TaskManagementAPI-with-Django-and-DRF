from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class User(AbstractUser):
    email = models.EmailField(unique=True)
    bio = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)
    # username = models.CharField(max_length=255, unique=True)
    # password = models.UUIDField()
    # is_staff = models.BooleanField(default=False)


TASK_PRIORITY_CHOICES = [
    ('L', 'Low'),
    ('M', 'Medium'),
    ('H', 'High')
]

STATUS_CHOICES = [
    ('P', 'Pending'),
    ('OP', 'ON Progress'),
    ('D', 'Done')
]

class Task(models.Model):    
    title = models.CharField(max_length=255)
    description = models.TextField()
    deadline = models.DateTimeField()
    priority = models.CharField(max_length=1, choices=TASK_PRIORITY_CHOICES)
    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default='P')
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='created_tasks')
    assigned_to = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='assigned_tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)