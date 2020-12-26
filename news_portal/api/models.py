from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Custom user model"""

    email = models.EmailField(blank=False, unique=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    is_banned = models.BooleanField(default=False)

    def __str__(self):
        return self.email


class News(models.Model):
    """News model"""

    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(blank=True, verbose_name='Контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-created_at']


class CommentToNews(models.Model):
    """Comment model"""

    text = models.TextField(max_length=5000, verbose_name='Содержание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    news = models.ForeignKey(
        News,
        on_delete=models.CASCADE,
        verbose_name='Новость'
    )
    author = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.text[30:]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['-created_at']

