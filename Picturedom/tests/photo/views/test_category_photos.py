from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from Picturedom.photo.models import Category, Photo


class TestCategoryPhotos(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')
        self.category2 = Category.objects.create(title='cat2')
        # first photo
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )
        # second photo
        self.photo2 = Photo.objects.create(
            image=SimpleUploadedFile("file2.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )
        # 3rd photo different category
        self.photo3 = Photo.objects.create(
            image=SimpleUploadedFile("file2.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category2,
        )

    def test_category_photos_GET__success(self):
        response = self.client.get(reverse('photo category', args=[self.category.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/photo_category.html')
        self.assertEqual(len(response.context['photos']), 2)
