from rest_framework.permissions import BasePermission


class IsOwnerOrIsSuperuser(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user == obj.user or request.user.is_superuser:
            return True
        return False