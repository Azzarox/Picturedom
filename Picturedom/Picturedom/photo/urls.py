from django.urls import path

from Picturedom.photo.views import homepage_photos, create_photo, photo_comments, add_comment, edit_comment, \
    delete_comment, dislike_comment, like_comment

urlpatterns = (
    path('', homepage_photos, name='homepage photos'),
    path('photo/create/', create_photo, name='create photo'),
    path('photo/<int:pk>/', photo_comments, name='photo comments'),
    path('photo/comments/<int:pk>/', add_comment, name='add comment'),
    path('photo/comments/edit/<int:pk>/', edit_comment, name='edit comment'),
    path('photo/comments/delete/<int:pk>/', delete_comment, name='delete comment'),
    path('photo/comments/like/<int:pk>/', like_comment, name='like comment'),
    path('photo/comments/dislike/<int:pk>/', dislike_comment, name='dislike comment'),
)
