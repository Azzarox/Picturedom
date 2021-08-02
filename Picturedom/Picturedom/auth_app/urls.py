from django.urls import path

from Picturedom.auth_app.views import register_user

urlpatterns = (
    path('register/', register_user, name='register'),
)
