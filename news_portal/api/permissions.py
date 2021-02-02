from rest_framework.permissions import BasePermission, SAFE_METHODS


class ReadOnly(BasePermission):
    """
    Разрешены только безопасные методы 'GET', 'HEAD', 'OPTIONS'
    """
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class IsAuthenticatedAndNotBanned(BasePermission):
    """
    Доступ для аутентифицированных и не заблокированных пользователей
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and not request.user.is_banned)


