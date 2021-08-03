from django.contrib.auth.models import User
from django.core.validators import EmailValidator, MaxLengthValidator, validate_image_file_extension
from django.db import models

from Picturedom.core.validators import validate_profile_names_are_only_letters, validate_profile_age, \
    validate_email_ending, validate_profile_image_file_size


class Profile(models.Model):
    first_name = models.CharField(max_length=10, blank=True, validators=[validate_profile_names_are_only_letters, ])
    last_name = models.CharField(max_length=10, blank=True, validators=[validate_profile_names_are_only_letters, ])
    age = models.PositiveIntegerField(default=0, validators=[validate_profile_age])
    email = models.EmailField(blank=True, validators=[MaxLengthValidator(20), EmailValidator, validate_email_ending])
    image = models.ImageField(upload_to='profile', blank=True,
                              validators=[validate_profile_image_file_size, validate_image_file_extension])
    user = models.OneToOneField(
        User,
        primary_key=True,
        on_delete=models.CASCADE,
    )
