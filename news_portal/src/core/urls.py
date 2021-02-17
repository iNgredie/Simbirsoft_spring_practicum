from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CreateCommentToNewsView, CreateNewsViewSet

urlpatterns = [
    path(
        "comment/", CreateCommentToNewsView.as_view({"get": "list", "post": "create"})
    ),
    path(
        "comment/<int:pk>/",
        CreateCommentToNewsView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
]

router = DefaultRouter()
router.register(r"news", CreateNewsViewSet)

urlpatterns += router.urls
