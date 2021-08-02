from django.urls import path

from Picturedom.photo.views import homepage_photos

urlpatterns = (
    path('', homepage_photos, name='homepage photos'),
)