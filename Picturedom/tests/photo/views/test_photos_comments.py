from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.contrib.auth.models import User
from Picturedom.photo.models import Category, Photo


class TestPhotoDetailView(TestCase):

    def test_photo_detail(self):
        user = User(username='user', password='pass')
        user.save()

        category = Category(title='category')
        category.save()

        photo = Photo(
            image=SimpleUploadedFile(
                name='test_image.jpg', content=b'', content_type='image/jpeg'),
            posted_at=timezone.now,
            posted_by=user,
            category=category
        )
        photo.save()

        response = self.client.get(reverse('photo comments', kwargs={'pk': photo.id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed('photos/comments.html')


