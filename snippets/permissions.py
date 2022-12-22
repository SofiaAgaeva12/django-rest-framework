from rest_framework import permissions


class Permission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.merhod in permissions.SAFE_METHODS and request.user:
            return True

        return request.user.is_staff
