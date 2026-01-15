from django.urls import path

from src.profile_user.views import profile_details

urlpatterns = (
    path('user/profile', profile_details, name='profile'),
)

import src.profile_user.signals
