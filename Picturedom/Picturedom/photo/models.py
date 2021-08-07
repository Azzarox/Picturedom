from django.contrib.auth.models import User
from django.core.validators import validate_image_file_extension
from django.db import models
from django.utils.timezone import now
from Picturedom.core.validators import *


class Category(models.Model):
    title = models.CharField(max_length=10)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.title


class Photo(models.Model):
    image = models.ImageField(upload_to='images', validators=[validate_image_file_size, validate_image_file_extension])
    posted_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    posted_at = models.DateTimeField(auto_now_add=True)


class PhotoLike(models.Model):
    image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    content = models.TextField(max_length=200, validators=[validate_against_forbidden_words])
    posted_at = models.DateTimeField(default=now)
    comment_image = models.ForeignKey(Photo, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.content


class CommentLike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class CommentDislike(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
