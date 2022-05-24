from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Post
from django.views.generic import TemplateView
from .forms import CommentForm

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
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request, 
            'details.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "Comment_form": CommentForm()
            },
        )

    def post(self,request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        user_comments = CommentForm(data=request.POST)   

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment_form.instance.email = request.user.email
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request, 
            'details.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "Comment_form": CommentForm()
            },
        )