from django import forms
from Picturedom.photo.models import Photo


class PhotoForm(forms.ModelForm):
    """
    The init removes the '-----' visualisation when there is no category chosen.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].empty_label = None

    class Meta:
        model = Photo
        fields = ('image', 'category')
        labels = {
            'image': 'Add Image',
            'category': 'Choose a category',
        }
        widgets = {
            'category': forms.RadioSelect()}
