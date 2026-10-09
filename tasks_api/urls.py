from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, CommentViewSet

router = DefaultRouter()
router.register('', TaskViewSet, basename='task')


urlpatterns = router.urls