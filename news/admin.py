from django.contrib import admin
from .models import Post, Comment

admin.site.register(Post)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('name', 'body')
admin.site.register(Comment, CommentAdmin)