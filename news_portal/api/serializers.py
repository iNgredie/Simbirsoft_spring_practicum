from rest_framework import serializers

from .models import News, CommentToNews


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class CommentToNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentToNews
        fields = '__all__'