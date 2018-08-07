from django import forms

from .models import FourWords


class AddNewWord(forms.Form):
    word = forms.CharField(label='Word', max_length=100)

