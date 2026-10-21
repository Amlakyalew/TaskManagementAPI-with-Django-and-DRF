from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import TaskViewSet, TaskStatusViewSet, CommentViewSet, RegisterViewSet, UserViewSet


router = DefaultRouter()
router.register('tasks', TaskViewSet, basename='tasks')
router.register('auth/users', UserViewSet, basename='users')

tasks_router = routers.NestedDefaultRouter(router, 'tasks', lookup='task')
tasks_router.register('comments', CommentViewSet, basename='task-comments')



urlpatterns = [
            path('tasks/<int:task_pk>/status/', TaskStatusViewSet.as_view({'get': 'retrieve', 'patch': 'partial_update'})),
            path('auth/register/', RegisterViewSet.as_view(), name='register'),
            ] + router.urls + tasks_router.urls