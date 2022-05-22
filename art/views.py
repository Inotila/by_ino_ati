from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'

class PaintingPage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-completed_on')
    template_name = 'paintings.html'

class InkPage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-completed_on')
    template_name = 'ink.html'

class PencilPage(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-completed_on')
    template_name = 'pencil.html'