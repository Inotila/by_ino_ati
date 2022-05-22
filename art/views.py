from django.shortcuts import render
from django.views import generic
from .models import Post
from django.views.generic import TemplateView

class HomePage(TemplateView):
    template_name = 'index.html'