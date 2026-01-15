from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from src.photo.forms import PhotoCommentForm
from src.photo.models import Category, Photo, Comment


class TestCommentForm(TestCase):
    def setUp(self):
        self.user = User.objects.create(
            username='User', password='Pass'
        )
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            id=1,
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )

    def test_save__commit_false__return_comment(self):
        data = {
            'image_pk': 1,
            'content': 'content',
        }
        form = PhotoCommentForm(data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.comment_image, self.photo)

    def test_save__commit_true__saves_in_db(self):
        self.client.login(username='User', password='Pass')
        data = {
            'image_pk': 1,
            'content': 'content',
        }
        form = PhotoCommentForm(data)
        self.assertTrue(form.is_valid())
        comment = form.save(commit=False)
        self.assertEqual(comment.content, 'content')
        self.assertEqual(comment.comment_image, self.photo)
        comment.user = self.user
        comment.save()
        self.assertIsInstance(comment, Comment)
        self.assertEqual(comment.comment_image, self.photo)
        self.assertEqual(Comment.objects.count(), 1)
        self.assertEqual(self.photo.comment_set.count(), 1)
