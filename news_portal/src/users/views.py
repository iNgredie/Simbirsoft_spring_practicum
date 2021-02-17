from rest_framework import mixins, viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser

from src.users.models import CustomUser
from src.users.serializers import CustomUserSerializer


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
