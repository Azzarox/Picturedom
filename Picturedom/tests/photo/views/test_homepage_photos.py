from django.urls import reverse
from django.test import TestCase


class TestHomepageListPhotosView(TestCase):

    def test_list_photos_view_GET(self):
        response = self.client.get(reverse('homepage photos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('photos/homepage_photos.html')
