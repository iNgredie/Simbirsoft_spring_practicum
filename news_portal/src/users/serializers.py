from rest_framework import serializers

from src.core.models import CustomUser


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализация пользователей
    """

    class Meta:
        model = CustomUser
        fields = "__all__"
