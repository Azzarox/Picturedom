from django import forms

from Picturedom.core.validators import validate_bot_field


class BotCatcherMixin(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['bot_cather'] = forms.CharField(
            widget=forms.HiddenInput(),
            required=False,
            validators=[validate_bot_field]
        )
