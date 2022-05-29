from django.test import TestCase
from .forms import CommentForm

class TestCommentForm(TestCase):

    def test_text_is_required(self):
        form = CommentForm({'text':''})
        self.assertFalse(form.is_valid())
        self.assertIn('text', forms.errors.keys())
    

    def test_field_is_explicit_in_form_metaclass(self):
        from = CommentForm()
        self.assertEqual(from.Meta.Fields, ['body'])