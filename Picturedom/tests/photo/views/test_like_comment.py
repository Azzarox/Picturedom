from django.test import TestCase
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse
from django.contrib.messages import get_messages
from Picturedom.photo.models import Category, Photo, Comment, CommentLike


class TestCommentLikeView(TestCase):

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

    def test_comment_POST_like_success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('like comment', args=[self.comment.id]), data=None)
        comment_likes = self.photo.comment_set.first().commentlike_set.count()
        self.assertEqual(comment_likes, 1)
        self.assertEqual(response.status_code, 302)

    def test_comment_POST_like__failed(self):
        self.client.force_login(self.user)
        like = CommentLike(
            comment=self.comment,
            user=self.user,
        )
        like.save()

        response = self.client.post(reverse('like comment', args=[self.comment.id]), data=None)
        comment_likes = self.photo.comment_set.first().commentlike_set.count()

        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have already liked this comment')
        self.assertEqual(comment_likes, 1)
        self.assertEqual(response.status_code, 302)
