from django.contrib import admin

from .models import CustomUser, CommentToNews

admin.site.register(CustomUser)
admin.site.register(CommentToNews)



