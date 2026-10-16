from rest_framework.permissions import BasePermission

class IsCommentCreatorOrAdmin(BasePermission):
    """
    For comments
    To check whether the comment is created by the current user or not, or is admin or not
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.user or request.user.is_staff)


class IsTaskCreatorOrAdmin(BasePermission):
    """
    For tasks
    To check whether the comment is created by the current user or not, or is admin or not
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.created_by or request.user.is_staff)

class IsTaskCreator(BasePermission):
    """
    Checking whether the user is task creator or not
    """
    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.created_by)