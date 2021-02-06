from rest_framework import viewsets, generics, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import News, CustomUser, CommentToNews
from .permissions import ReadOnly, IsAuthenticatedAndNotBanned
from .serializers import NewsSerializer, CustomUserSerializer, CreateCommentToNewsSerializer


class MixedPermission:
    """ Миксин permissions для action
    """

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]
        except KeyError:
            return [permission() for permission in self.permission_classes]


class CreateNewsViewSet(viewsets.ModelViewSet):
    """
    CRUD и вывод новостей
    """
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser | ReadOnly]


class CreateCommentToNewsView(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              MixedPermission,
                              viewsets.GenericViewSet):
    """
    CRUD и вывод комментариев к новостям
    """
    queryset = CommentToNews.objects.filter(level__lte=5)
    serializer_class = CreateCommentToNewsSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAuthenticated]
    permission_classes_by_action = {'list': [IsAuthenticated],
                                    'retrieve': [IsAuthenticated],
                                    'create': [IsAuthenticatedAndNotBanned],
                                    'update': [IsAdminUser],
                                    'destroy': [IsAdminUser]}


class ListCustomUsers(generics.UpdateAPIView):
    """
    Вывод и Update пользователей
    """
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [IsAdminUser]
