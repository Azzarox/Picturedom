from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.messages import get_messages
from src.photo.models import Category, CommentDislike, Photo, Comment


class TestDislikeCommentView(TestCase):

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

    def test_comment_POST_dislike__success(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('dislike comment', args=[self.comment.id]))
        comment_dislikes = self.photo.comment_set.first().commentdislike_set.count()
        self.assertEqual(comment_dislikes, 1)
        self.assertEqual(response.status_code, 302)

    def test_comment_POST_dislike__failed(self):
        self.client.force_login(self.user)
        dislike = CommentDislike(
            comment=self.comment,
            user=self.user,
        )
        dislike.save()

        response = self.client.post(reverse('dislike comment', args=[self.comment.id]), data=None)
        comment_dislikes = self.photo.comment_set.first().commentdislike_set.count()
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), 'You have already disliked this comment')
        self.assertEqual(comment_dislikes, 1)
        self.assertEqual(response.status_code, 302)
