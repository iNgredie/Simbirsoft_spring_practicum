from django.urls import path

from src.users.views import ListRetrieveUpdateCustomUser

urlpatterns = [
    path("user/", ListRetrieveUpdateCustomUser.as_view({"get": "list"})),
    path(
        "user/<int:pk>/",
        ListRetrieveUpdateCustomUser.as_view(
            {
                "get": "retrieve",
                "put": "update",
            }
        ),
    ),
]
