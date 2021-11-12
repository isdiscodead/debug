from django.forms import ModelForm
from django import forms

from requestapp.models import Quest


class QuestCreationForm(ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'editable text-left',
                                                           'style': 'height: auto;'}))

    class Meta:
        model = Quest
        fields = ['title', 'img', 'location', 'start_price', 'end_price', 'content']
