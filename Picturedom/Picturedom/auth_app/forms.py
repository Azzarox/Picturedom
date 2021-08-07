from django.contrib.auth.forms import UserCreationForm

from Picturedom.core.mixins import BotCatcherMixin


class RegisterUserForm(BotCatcherMixin, UserCreationForm):
    pass
