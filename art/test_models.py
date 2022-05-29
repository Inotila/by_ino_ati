from django.test import TestCase
from . models import Post


class TestDjango(TestCase):

    def test_done_defaults_to_false(self):
        post = Post.objects.create(name='Test post')
        self.assertFalse(post.done)