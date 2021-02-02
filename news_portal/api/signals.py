from django.core.mail import send_mail
from django.db.models import F
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from config.settings import EMAIL_HOST_USER
from .models import CommentToNews, CustomUser


@receiver(pre_save, sender=CustomUser)
def user_ban(sender, instance, *args, **kwargs):
    """
    Сообщение пользователю на почту, если его забанят
    """
    users = CustomUser.objects.filter(email=instance.email, is_banned=False)
    if instance in users:
        if instance.is_banned:
            send_mail(
                'From Admin',
                'You are banned',
                EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False,
            )


@receiver(pre_save, sender=CustomUser)
def user_unban(sender, instance, *args, **kwargs):
    """
    Сообщение пользователю на почту, если его разбанят
    """
    users = CustomUser.objects.filter(email=instance.email, is_banned=True)
    if instance in users:
        if not instance.is_banned:
            send_mail(
                'From Admin',
                'You are unbanned',
                EMAIL_HOST_USER,
                [instance.email],
                fail_silently=False,
            )


@receiver(post_save, sender=CommentToNews)
def comment_create(sender, instance, *args, **kwargs):
    """
    Сообщение пользователю на почту, если кто-то ответил на его комментарий.
    """
    if F(instance.children) + 1:
        message = f'{instance.author} replied: {instance.text}'
        send_mail(
            'From Admin',
            message,
            EMAIL_HOST_USER,
            [instance.author],
            fail_silently=False,
        )
