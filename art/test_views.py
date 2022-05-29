from django.test import TestCase

class TestViews(TestCase):
    
    def test_get_home_page(self):
        response = self.client.get('/')
        self.assertEqual(responst.status_code, 200)
        self.assertTemplateUsed(response, 'templates/index.html')

    def test_get_art_views(self):

    def test_get_art_details(self):
    
    def test_like_post(self):

    def test_add_comment(self):

    def test_edit_comment(self):
    
    def test_delete_comment(self):

    def test_join_mail_list(self):