from django.shortcuts import render
from django.views import generic
from .models import Post

class PostGird(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('completed_on')
    template_name = 'index.html'