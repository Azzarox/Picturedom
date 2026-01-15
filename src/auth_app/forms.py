from django.contrib.auth.forms import UserCreationForm

from src.core.mixins import BotCatcherMixin


class RegisterUserForm(BotCatcherMixin, UserCreationForm):
    pass
