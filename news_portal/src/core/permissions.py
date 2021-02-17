from rest_framework.permissions import SAFE_METHODS, BasePermission


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
        return bool(
            request.user
            and request.user.is_authenticated
            and not request.user.is_banned
        )


class MixedPermission:
    """Миксин permissions для action"""

    def get_permissions(self):
        try:
            return [
                permission()
                for permission in self.permission_classes_by_action[self.action]
            ]
        except KeyError:
            return [permission() for permission in self.permission_classes]
