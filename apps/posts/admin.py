from django.contrib import admin

from apps.posts.models import Post, Like

admin.site.register(Post)
admin.site.register(Like)
