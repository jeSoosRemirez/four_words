from django.db import models

WORD_CHOICES = (
    (1, 'noun'),
    (2, 'adjective'),
    (3, 'adverb'),
    (4, 'verb'),
)


class FourWords(models.Model):
    noun = models.CharField(max_length=50, blank=True)
    noun_desription = models.TextField(max_length=230, blank=True)
    noun_example = models.TextField(max_length=230, blank=True)
    noun_translate = models.CharField(max_length=50, blank=True)
    adjective = models.CharField(max_length=50, blank=True)
    adjective_desription = models.TextField(max_length=230, blank=True)
    adjective_example = models.TextField(max_length=230, blank=True)
    adjective_translate = models.CharField(max_length=50, blank=True)
    adverb = models.CharField(max_length=50, blank=True)
    adverb_desription = models.TextField(max_length=230, blank=True)
    adverb_example = models.TextField(max_length=230, blank=True)
    adverb_translate = models.CharField(max_length=50, blank=True)
    verb = models.CharField(max_length=50, blank=True)
    verb_desription = models.TextField(max_length=230, blank=True)
    verb_example = models.TextField(max_length=230, blank=True)
    verb_translate = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.noun} | {self.adjective} | {self.adverb} | {self.verb}'


class OneWord(models.Model):

    word = models.CharField(max_length=50)
    word_type = models.IntegerField(choices=WORD_CHOICES, default=1)

    def __str__(self):
        return f'{self.word} | {self.word_type}'
