from django.forms import ModelForm
from django import forms

from hunterapp.models import Hunter


class HunterCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Hunter
        fields = ['title', 'location', 'content']
