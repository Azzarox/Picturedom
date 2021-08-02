from django.contrib.auth.models import User
from Picturedom.photo.models import Category, Photo
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse


class TestAddCommentView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )

    def test_comment_create_POST(self):
        self.client.force_login(self.user, backend=None)  # login the user
        data = {
            'image_pk': self.photo.id,
            'content': 'content',
        }
        response = self.client.post(reverse('add comment', args=[self.photo.id]), data)
        comment_user = self.photo.comment_set.get(user=self.user).user
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.photo.comment_set.count(), 1)
        self.assertEqual(comment_user, self.user)

    def test_comment_create_POST_error(self):
        self.client.force_login(self.user, backend=None)  # login the user
        data = {
            'id': 1,
            'image_pk': 1,
            'content': 'suck',
        }
        response = self.client.post(reverse('add comment', args=[self.photo.id]), data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.photo.comment_set.count(), 0)
