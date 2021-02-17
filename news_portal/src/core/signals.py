from django.core.mail import send_mail
from django.db.models import F
from django.db.models.signals import post_save
from django.dispatch import receiver

from config.settings import EMAIL_HOST_USER

from .models import CommentToNews


@receiver(post_save, sender=CommentToNews)
def comment_create(sender, instance, *args, **kwargs):
    """
    Сообщение пользователю на почту, если кто-то ответил на его комментарий.
    """
    if F(instance.children) + 1:
        message = f"{instance.author.username} replied: {instance.text}"
        send_mail(
            "From Admin",
            message,
            EMAIL_HOST_USER,
            [instance.parent.author.email],
            fail_silently=False,
        )
