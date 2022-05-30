"""forms imports"""
from django import forms
from .models import Comment, MailingList


class CommentForm(forms.ModelForm):
    """creates the form for leaving a comment"""
    class Meta:
        """makes only the comments and the body show"""
        model = Comment
        fields = ('body',)


class MailForm(forms.ModelForm):
    """creates the form for joing the mailing list"""
    class Meta:
        model = MailingList
        fields = ('join', )
