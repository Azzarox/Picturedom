from django.urls import reverse
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.utils import timezone
from django.contrib.auth.models import User
from src.photo.models import Category, Photo, PhotoLike


class TestPhotoDetailView(TestCase):

    def test_photo_comments(self):
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

    def test_photo_detail__has_liked_image__authenticated(self):
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
        photo_like = PhotoLike(
            user=user,
            image=photo,
        )
        photo_like.save()
        self.client.force_login(user)
        response = self.client.get(reverse('photo comments', kwargs={'pk': photo.id}))
        is_liked_by_user = photo.photolike_set.filter(user=user).exists()
        self.assertTrue(is_liked_by_user)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['is_liked'], is_liked_by_user)
        self.assertTemplateUsed('photos/comments.html')




