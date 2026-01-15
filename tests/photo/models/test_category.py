from django.test import TestCase

from src.photo.models import Category


class TestCommentModel(TestCase):

    def test_category_str__success(self):
        category = Category.objects.create(title='category')
        self.assertEqual(str(category), 'category')
