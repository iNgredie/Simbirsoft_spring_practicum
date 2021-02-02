from rest_framework import serializers

from .models import News, CommentToNews, CustomUser


class FilterCommentListSerializer(serializers.ListSerializer):
    """
    Фильтр комментариев, только parents
    """
    def to_representation(self, data):
        data = data.filter(parent=None)
        return super().to_representation(data)


class RecursiveSerializer(serializers.Serializer):
    """
    Вывод рекурсивно children
    """
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CreateCommentToNewsSerializer(serializers.ModelSerializer):
    """
    Сериализация CRUD комментов
    """
    class Meta:
        model = CommentToNews
        fields = '__all__'


class CommentToNewsSerializer(serializers.ModelSerializer):
    """
    Сериализация отзывов к новости
    """
    text = serializers.SerializerMethodField()
    author = serializers.CharField(source='author.username')
    news = serializers.CharField(source='news.title')
    children = RecursiveSerializer(many=True)

    def get_text(self, obj):
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = CommentToNews
        fields = ('id', 'author', 'news', 'text', 'created_at', 'children', 'level')


class NewsSerializer(serializers.ModelSerializer):
    """
    Сериализация новостей
    """
    comments = CommentToNewsSerializer(many=True, read_only=True)

    class Meta:
        model = News
        fields = ('title', 'content', 'created_at', 'updated_at', 'author', 'comments')


class CustomUserSerializer(serializers.ModelSerializer):
    """
    Сериализация пользователей
    """
    class Meta:
        model = CustomUser
        fields = '__all__'
