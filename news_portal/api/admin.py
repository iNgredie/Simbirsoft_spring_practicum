from django.contrib import admin

from .models import CommentToNews, CustomUser

admin.site.register(CustomUser)
admin.site.register(CommentToNews)
