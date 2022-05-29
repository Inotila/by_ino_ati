"""forms imports"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """handles what should be shown in/from comment form"""
    class Meta:
        """makes only the comments and the body show"""
        model = Comment
        fields = ('body',)
