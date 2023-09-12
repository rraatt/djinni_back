from rest_framework.permissions import BasePermission


class IsEmployer(BasePermission):
    """
    Allows access only to employers.
    """
    def has_permission(self, request, view):
        return not request.user.user_type.has_additional_profile
