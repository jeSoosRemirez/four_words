from django import forms

from .models import FourWords


WORD_CHOICES = (
    (1, 'noun'),
    (2, 'adjective'),
    (3, 'adverb'),
    (4, 'verb'),
)


class AddNewWord(forms.Form):
    word = forms.CharField(label='Word', max_length=100)


class EditFourWords(forms.ModelForm):

    class Meta:
        model = FourWords
        fields = ('noun', 'adjective', 'adverb', 'verb', 'other',
                  'noun_description', 'adjective_description', 'adverb_description', 'verb_description',
                  'other_description',
                  'noun_example', 'adjective_example', 'adverb_example', 'verb_example', 'other_example',
                  'noun_translate', 'adjective_translate', 'adverb_translate', 'verb_translate', 'other_translate'
                  )
