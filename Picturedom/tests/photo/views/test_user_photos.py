from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from Picturedom.photo.models import Category, Photo


class TestUserPhotosView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )

    def test_user_photos_GET__success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('user photos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/user_photos.html')