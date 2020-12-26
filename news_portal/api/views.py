from rest_framework import generics, viewsets
from rest_framework.permissions import IsAuthenticated


from .models import News, CustomUser, CommentToNews
from .serializers import NewsSerializer, CommentToNewsSerializer


class ListNews(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class CommentToNewsView(viewsets.ModelViewSet):
    queryset = CommentToNews.objects.all()
    serializer_class = CommentToNewsSerializer
    permission_classes = [IsAuthenticated]
