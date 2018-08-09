from django.db import models

from django.conf import settings

from django import forms


WORD_CHOICES = (
    (1, 'noun'),
    (2, 'adjective'),
    (3, 'adverb'),
    (4, 'verb'),
)




class FourWords(models.Model):
    noun = models.CharField(max_length=50, blank=True)
    noun_description = models.TextField(max_length=230, blank=True)
    noun_example = models.TextField(max_length=230, blank=True)
    noun_translate = models.CharField(max_length=50, blank=True)
    adjective = models.CharField(max_length=50, blank=True)
    adjective_description = models.TextField(max_length=230, blank=True)
    adjective_example = models.TextField(max_length=230, blank=True)
    adjective_translate = models.CharField(max_length=50, blank=True)
    adverb = models.CharField(max_length=50, blank=True)
    adverb_description = models.TextField(max_length=230, blank=True)
    adverb_example = models.TextField(max_length=230, blank=True)
    adverb_translate = models.CharField(max_length=50, blank=True)
    verb = models.CharField(max_length=50, blank=True)
    verb_description = models.TextField(max_length=230, blank=True)
    verb_example = models.TextField(max_length=230, blank=True)
    verb_translate = models.CharField(max_length=50, blank=True)
    other = models.CharField(max_length=50, blank=True)
    other_description = models.TextField(max_length=230, blank=True)
    other_example = models.TextField(max_length=230, blank=True)
    other_translate = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField('date published')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.noun} | {self.adjective} | {self.adverb} | {self.verb} | {self.author.username}'


class OneWord(models.Model):

    word = models.CharField(max_length=50)
    word_type = models.IntegerField(choices=WORD_CHOICES, default=1)

    def __str__(self):
        return f'{self.word} | {self.word_type}'
