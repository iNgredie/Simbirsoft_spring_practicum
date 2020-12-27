from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentToNewsView, CreateNewsViewSet

urlpatterns = []

router = DefaultRouter()
router.register(r'comment', CommentToNewsView)
router.register(r'news', CreateNewsViewSet)

urlpatterns += router.urls