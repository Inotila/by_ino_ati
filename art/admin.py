from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status',)
    search_fields = ['title', 'completed_on']
    list_display = ('title', 'status', 'completed_on')
    # summernote_fields = ('title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email', 'created_on']
    list_filter = ('created_on',)
