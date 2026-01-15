from django import forms

from src.core.mixins import BotCatcherMixin
from src.profile_user.models import Profile


class ProfileForm(BotCatcherMixin, forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'image': forms.FileInput(),
            'first_name': forms.TextInput(attrs={'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'placeholder': 'Last Name'}),
            'age': forms.NumberInput(attrs={'placeholder': 'Age'}),
            'email': forms.TextInput(attrs={'placeholder': 'Email'}),
        }


class DeleteProfileImageForm(forms.Form):
    delete_image = forms.CharField(widget=forms.CheckboxInput)
