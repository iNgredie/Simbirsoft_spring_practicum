from rest_framework import generics, mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from .models import CommentToNews, CustomUser, News
from .permissions import IsAuthenticatedAndNotBanned, ReadOnly
from .serializers import (
    CreateCommentToNewsSerializer,
    CustomUserSerializer,
    NewsSerializer,
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


class CreateNewsViewSet(viewsets.ModelViewSet):
    """
    CRUD новостей для админа.
    Получение списка новостей для авторизованных
    и неавторизованных пользователей.
    """

    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser | ReadOnly]


class CreateCommentToNewsView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    MixedPermission,
    viewsets.GenericViewSet,
):
    """
    CRUD комментариев для админа.
    Возможность оставить комментарий к новости для авторизованного
    и не забаненного пользователя
    Вывод комментариев, уровень вложенности которых меньше или ровно 5
    """

    queryset = CommentToNews.objects.filter(level__lte=5)
    serializer_class = CreateCommentToNewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAuthenticatedAndNotBanned],
        "update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }


class ListRetrieveUpdateCustomUser(
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    """
    Вывод и Update пользователей только для админа
    """

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
