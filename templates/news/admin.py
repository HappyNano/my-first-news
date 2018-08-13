from django.contrib import admin
from .models import Post, Small_post, Comment

admin.site.register(Small_post)
admin.site.register(Post)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'body', 'post', 'created', 'active')
    list_filter = ('active', 'created', 'updated')
    search_fields = ('user', 'body')
admin.site.register(Comment, CommentAdmin)