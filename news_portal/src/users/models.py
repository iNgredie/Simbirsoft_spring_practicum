from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model"""

    email = models.EmailField(blank=False, unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.email
