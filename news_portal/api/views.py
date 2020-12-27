from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser, SAFE_METHODS, BasePermission

from .models import News, CustomUser, CommentToNews
from .serializers import NewsSerializer, CommentToNewsSerializer, CustomUserSerializer


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class CreateNewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [IsAdminUser | ReadOnly]


class CommentToNewsView(viewsets.ModelViewSet):
    queryset = CommentToNews.objects.all()
    serializer_class = CommentToNewsSerializer
    permission_classes = [IsAuthenticated]


class ListCustomUsers(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [IsAdminUser]