from django.urls import path

from Picturedom.profile_user.views import profile_details

urlpatterns = (
    path('user/profile', profile_details, name='profile'),
)

import Picturedom.profile_user.signals
