from .models import Text
from django.forms import ModelForm


class TextForm(ModelForm):
    class Meta:
        model = Text
        fields = ['title', 'text']
