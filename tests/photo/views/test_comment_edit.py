from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from src.photo.models import Category, Photo, Comment


class TestCommentEdit(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('user', 'email', 'pass')
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )
        self.comment = Comment.objects.create(
            content='content',
            comment_image=self.photo,
            user=self.user,
        )

    def test_comment_edit_POST__success(self):
        self.client.force_login(self.user)
        data = {
            'content': 'content changed'
        }
        response = self.client.post(reverse('edit comment', args=[self.comment.id]), data=data)
        changed_comment = self.photo.comment_set.get(user=self.user)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(changed_comment.content, 'content changed')

    def test_comment_edit_GET__success(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('edit comment', args=[self.comment.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'photos/edit_comment.html')
