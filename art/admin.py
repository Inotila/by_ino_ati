"""admin imports"""
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Comment, MailingList


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):
    """handles the admin pannel in the backend"""
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status',)
    search_fields = ['title', 'completed_on']
    list_display = ('title', 'status', 'completed_on')
    # summernote_fields = ('title')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """handles the admin pannel in the backend"""
    list_display = ('name', 'email', 'created_on')
    search_fields = ['name', 'email', 'created_on']
    list_filter = ('created_on',)


@admin.register(MailingList)
class MailingListAdmin(admin.ModelAdmin):
    """handles the admin pannel in the backend"""
    list_display = ('user', 'email', 'join', 'joined_on')
    search_fields = ['user', 'join', 'joined_on']
    list_filter = ('joined_on',)

    @admin.display()
    def email(self, response):
        return response.user.email
