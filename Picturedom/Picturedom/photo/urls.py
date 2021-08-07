from django.urls import path

from Picturedom.photo.views import homepage_photos, create_photo, photo_comments, add_comment, edit_comment, \
    delete_comment, dislike_comment, like_comment, user_photos, photo_category, photo_like

urlpatterns = (
    path('', homepage_photos, name='homepage photos'),
    path('user/photos/', user_photos, name='user photos'),
    path('photo/create/', create_photo, name='create photo'),
    path('photo/<int:pk>/', photo_comments, name='photo comments'),
    path('photo/like/<int:pk>', photo_like, name='photo like'),
    path('photo/comments/<int:pk>/', add_comment, name='add comment'),
    path('photo/comments/edit/<int:pk>/', edit_comment, name='edit comment'),
    path('photo/comments/delete/<int:pk>/', delete_comment, name='delete comment'),
    path('photo/comments/like/<int:pk>/', like_comment, name='like comment'),
    path('photo/comments/dislike/<int:pk>/', dislike_comment, name='dislike comment'),
    path('photo/categories/<int:pk>', photo_category, name='photo category'),

)
