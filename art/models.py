"""models imports"""
from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))
TYPE_OF_ART = (("painting", "Painting"), ("ink", "Ink"), ("pencil", "Pencil"))


class Post(models.Model):
    """this handles the data for the posts that the admin makes"""
    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100,  unique=True)
    type = models.CharField(max_length=20, choices=TYPE_OF_ART)
    completed_on = models.DateField(auto_now=False)
    featured_image = CloudinaryField('image', default='placeholder')
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='art_likes', blank=True)
    size = models.CharField(max_length=100, unique=False, default='cm')

    class Meta:
        """ this oders the post from oldest to news comments"""
        ordering: ['-completed_on']

    def __str__(self):
        return self.title

    def total_number_of_likes(self):
        """this counts the total number of likes"""
        return self.likes.count()


class Comment(models.Model):
    """handles the data for the comments users make"""
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """oders the comments from newsest to oldest"""
        ordering = ['created_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.name}"


class MailingList(models.Model):
    """collects data for users who joined the mail list"""
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=False)
    join = models.BooleanField(default=False, null=False)
    joined_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """oders the users on the date they joined"""
        ordering = ['joined_on']

    def __str__(self):
        return f"{self.user.username}"
