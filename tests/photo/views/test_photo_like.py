from django.contrib.auth.models import User
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from src.photo.models import Category, Photo, PhotoLike


class TestLikeImageView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')

        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )

    def test_like_image__increase_likes(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('photo like', kwargs={'pk': self.photo.id}))
        self.assertEqual(self.photo.photolike_set.count(), 1)
        self.assertEqual(response.status_code, 302)

    def test_like_image__decrease_likes(self):
        self.client.force_login(self.user)
        p = PhotoLike(
            image=self.photo,
            user=self.user,
        )
        p.save()
        response = self.client.get(reverse('photo like', kwargs={'pk': self.photo.id}))
        self.assertEqual(self.photo.photolike_set.count(), 0)
        self.assertEqual(response.status_code, 302)
