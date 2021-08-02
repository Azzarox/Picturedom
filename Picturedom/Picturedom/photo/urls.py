from django.urls import path

from Picturedom.photo.views import homepage_photos, create_photo, photo_comments, add_comment

urlpatterns = (
    path('', homepage_photos, name='homepage photos'),
    path('photo/create/', create_photo, name='create photo'),
    path('photo/<int:pk>/', photo_comments, name='photo comments'),
    path('photo/comments/<int:pk>/', add_comment, name='add comment'),
)