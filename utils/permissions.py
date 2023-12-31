from rest_framework import permissions
from authentication.apps import AuthenticationConfig as Conf


class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.user_type == Conf.USER_TYPE_ADMIN)


class IsMember(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user and request.user.user_type == Conf.USER_TYPE_USER)
