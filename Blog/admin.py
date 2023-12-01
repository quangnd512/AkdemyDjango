from django.contrib import admin
from .models import Blog, Comment

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'from_user', 'number_read')

class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'blog_id', 'user_id')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Comment, CommentAdmin)