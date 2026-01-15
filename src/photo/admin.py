from django.contrib import admin

from src.photo.models import Comment, CommentLike, CommentDislike, Photo, Category, PhotoLike

admin.site.register(Photo)
admin.site.register(PhotoLike)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(CommentLike)
admin.site.register(CommentDislike)
