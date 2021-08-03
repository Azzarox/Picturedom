from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from Picturedom.photo.models import Category, Photo, Comment


class TestCommentDeleteView(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile(
                "file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )
        self.comment = Comment.objects.create(
            content='content',
            comment_image=self.photo,
            user=self.user,
        )

    def test_comment_delete__success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('delete comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(self.photo.comment_set.count(), 0)
        self.assertIsNone(Comment.objects.first())
