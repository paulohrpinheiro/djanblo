from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"path": ("title",)}
    fields = ('title', 'path', 'subject', 'content', 'author')
