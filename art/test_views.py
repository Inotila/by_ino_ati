from django.test import TestCase
from .models import Comment


class TestViews(TestCase):
    
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/index.html')

    def test_get_art_views(self):
        response = self.client.get('art/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/art.html')

    def test_get_art_details(self):
        response = self.client.get('<slug:slug>/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/details.html')

    def test_like_post(self):
        response = self.client.post.like('<slug:slug>/', done=True)
        self.assertRedirects(response, '<slug:slug>/')

    def test_add_comment(self):
        response = self.client.post('<slug:slug>/', {'name': 'Test Comment'})
        self.assertRedirects(response, '<slug:slug>/')

    def test_edit_comment(self):
        comment = Comment.objects.create(body='test comment')
        response = self.client.get(f'edit/{comment.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'templates/details.html')

    def test_delete_comment(self):
        comment = Comment.objects.create(body='test comment')
        response = self.client.get(f'edit/{comment.id}')
        self.assertRedirects(response, '<slug:slug>/')

    # def test_join_mail_list(self):