from django import forms
from django.forms import widgets

from Picturedom.core.mixins import BotCatcherMixin
from Picturedom.photo.models import Photo, Comment


class PhotoForm(BotCatcherMixin, forms.ModelForm):
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


class PhotoCommentForm(BotCatcherMixin, forms.ModelForm):
    image_pk = forms.IntegerField(widget=forms.HiddenInput())

    class Meta:
        model = Comment
        fields = ('content',)
        labels = {
            'content': ''
        }

    def save(self, commit=True):
        image_pk = self.cleaned_data['image_pk']
        image = Photo.objects.get(pk=image_pk)
        comment = Comment(
            content=self.cleaned_data['content'],
            comment_image=image,
        )
        if commit:
            comment.save()

        return comment


class EditCommentForm(BotCatcherMixin, forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content', ]
        labels = {
            'content': 'Edit your comment'
        }
        widgets = {
            'content': widgets.Textarea(attrs={'style': 'height: 100px;'})
        }
