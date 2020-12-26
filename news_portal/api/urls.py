from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentToNewsView, ListNews

urlpatterns = [
    path('news', ListNews.as_view()),
]

router = DefaultRouter()
router.register(r'comment', CommentToNewsView)

urlpatterns += router.urls