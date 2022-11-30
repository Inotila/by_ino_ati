"""imports"""
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import TemplateView
from .models import Post, Comment, MailingList
from .forms import CommentForm, MailForm


def home(request):
    """class based view that displays the home page"""
    if request.user.is_authenticated:
        user = get_object_or_404(User, username=request.user)
        submitted_form = MailingList.objects.filter(user=user).count()
        mail_form = MailForm(request.POST, initial={'user': request.user})

        if request.method == "POST":
            if mail_form.is_valid():
                mail_form.instance.user = user
                mail_form.save()
                if request.POST.get("join"):
                    messages.success(
                        request,
                        "You have successfully joined the mailing list!")
                else:
                    messages.error(
                        request,
                        "You have select to not join the mailing list.")
                submitted_form = 1
    else:
        submitted_form = 0
        mail_form = MailForm()

    template = 'index.html'
    context = {
        "submitted_form": submitted_form,
        "mail_form": mail_form,
    }
    return render(request, template, context)


def art_views(request):
    """ function that displays post on art.html
    depending on what category they are listed as"""
    category = request.GET['category']
    all_art = Post.objects.filter(type=category, status=1)
    template = 'art.html'
    context = {
        'all_art': all_art,
        'category': category,
    }

    return render(request, template, context)


class ArtDetails(View):
    """ shows the post that has been clicked on"""
    def get(self, request, slug, *args, **kwargs):
        """this handles the like button when it has be clicked"""
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
        """ handles the comment form """
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
            messages.success(request, "You have successfully commented")
        else:
            messages.error(request, "Something went wrong,try again!")
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


def edit_comment(request, comment_id,):
    """
    this is handles the edit button. it gets the comment id from django.
    the redirect path need to be fixed to redirect back to the art details
    """
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        user_comments = CommentForm(request.POST, instance=)
        if user_comments.is_valid():
            user_comments.save()
            messages.success(request, "You have successfully updated comment")
            return redirect(reverse('art_details', args=[comment.post.slug]))
        messages.error(request, "Something went wrong,try again!")
    post = comment.post
    user_comments = CommentForm(instance=comment)
    context = {
        "user_comments": user_comments,
        'post': post,
        'comment': comment
    }

    return render(request, 'edit_comment.html', context)


def delete_comment(request, comment_id,):
    """ this deletes comments and
    redirects the the redirect need to be fixed"""
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "You have successfully deleted comment")
    return redirect(reverse('art_details', args=[comment.post.slug]))


class ArtLike(View):
    """ class bassed view that displays the likes """

    def post(self, request, slug):
        """handles post likes"""
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('art_details', args=[slug]))
