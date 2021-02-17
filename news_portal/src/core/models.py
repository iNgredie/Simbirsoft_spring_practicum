from django.db import models
from mptt.models import MPTTModel, TreeForeignKey
from rest_framework.exceptions import ValidationError

from src.users.models import CustomUser


class News(models.Model):
    """News model"""

    title = models.CharField(max_length=150, verbose_name="Наименование")
    content = models.TextField(blank=True, verbose_name="Контент")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Обновлено")
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Автор"
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class CommentToNews(MPTTModel):
    """Comment model"""

    MAX_TREE_DEPTH = 5
    text = models.TextField(max_length=5000, verbose_name="Содержание")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    news = models.ForeignKey(
        News, on_delete=models.CASCADE, verbose_name="Новость", related_name="comments"
    )
    author = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE, verbose_name="Автор"
    )
    parent = TreeForeignKey(
        "self",
        verbose_name="Родитель",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name="children",
    )

    def save(self, *args, **kwargs):
        if self.parent.level > self.MAX_TREE_DEPTH:
            raise ValidationError(
                {
                    "level": f"Comment can only be nested {self.MAX_TREE_DEPTH} levels deep"
                }
            )

    def __str__(self):
        return self.text[:30]

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-created_at"]
