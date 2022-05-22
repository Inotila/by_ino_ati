from django.shortcuts import render, get_object_or_404
from django.views import generic, View
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

class ArtDetails(View):

    def get(self,request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if posst.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'details.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked
            },
        )