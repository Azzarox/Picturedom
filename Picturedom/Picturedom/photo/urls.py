from django.urls import path

from Picturedom.photo.views import homepage_photos, create_photo

urlpatterns = (
    path('', homepage_photos, name='homepage photos'),
    path('photo/create/', create_photo, name='create photo'),
)