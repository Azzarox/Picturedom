from django.contrib.auth.models import User
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile

from Picturedom.photo.models import Category, Photo, Comment


class TestCommentModel(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='User', password='Pass'
        )
        self.category = Category.objects.create(title='category')
        self.photo = Photo.objects.create(
            image=SimpleUploadedFile("file.jpeg", b"file_content", content_type="image/jpeg"),
            posted_by=self.user,
            category=self.category,
        )

    def test_comment_str__success(self):
        comment = Comment.objects.create(
            content='comment',
            user=self.user,
            comment_image=self.photo,
        )
        comment.save()
        self.assertEqual(str(comment), 'comment')
