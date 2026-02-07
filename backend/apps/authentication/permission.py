from rest_framework.permissions import BasePermission

# from authentication.models import User


class RolePermission(BasePermission):
    def has_permission(self, request, view):
        user = request.user

        # Check if the user is authenticated
        if not user.is_authenticated:
            return False

        # Check if the user has the role of an admin (role = 1)
        if user.role != 1:
            return False

        return True
