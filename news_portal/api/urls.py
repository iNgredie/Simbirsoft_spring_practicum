from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CreateNewsViewSet, CreateCommentToNewsView, ListRetrieveUpdateCustomUser

urlpatterns = [
    path('comment/', CreateCommentToNewsView.as_view({'get': 'list', 'post': 'create'})),
    path('comment/<int:pk>/', CreateCommentToNewsView.as_view({
        'get': 'retrieve', 'put': 'update', 'delete': 'destroy'
    })),
    path('user/', ListRetrieveUpdateCustomUser.as_view({'get': 'list'})),
    path('user/<int:pk>/', ListRetrieveUpdateCustomUser.as_view({
        'get': 'retrieve', 'put': 'update',
    })),
]

router = DefaultRouter()
router.register(r'news', CreateNewsViewSet)

urlpatterns += router.urls