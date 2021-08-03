from django import forms

from Picturedom.profile_user.models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ('user',)
        widgets = {
            'image': forms.FileInput(),
        }


class DeleteProfileImageForm(forms.Form):
    delete_image = forms.CharField(widget=forms.CheckboxInput)
