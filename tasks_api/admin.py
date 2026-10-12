from django.contrib import admin
from django.conf import settings
from .models import User, Task, Comment

# Register your models here.
admin.site.site_header = 'Task Manager System Admin'

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    pass