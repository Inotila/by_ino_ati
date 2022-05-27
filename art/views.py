from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from django.views.generic import TemplateView
from .forms import CommentForm


class HomePage(TemplateView):
    template_name = 'index.html'


def art_views(request):
    category = request.GET['category']
    all_art = Post.objects.filter(type=category)
    template = 'art.html'
    context = {
        'all_art': all_art,
        'category': category,
    }

    return render(request, template, context)


class ArtDetails(View):

    def get(self, request, slug, *args, **kwargs):
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
                "user_comments": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        user_comments = CommentForm(data=request.POST)

        if user_comments.is_valid():
            user_comments.instance.email = request.user.email
            user_comments.instance.name = request.user.username
            user_comments.instance.email = request.user.email
            comment = user_comments.save(commit=False)
            comment.post = post
            comment.save()
        else:
            user_comments = CommentForm()

        return render(
            request,
            'details.html',
            {
                "post": post,
                "comments": comments,
                "liked": liked,
                "user_comments": CommentForm()
            },
        )


class ArtLike(View):

    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('art_details', args=[slug]))
