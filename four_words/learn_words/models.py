from django.db import models


class FourWords(models.Model):

    noun = models.CharField(max_length=50, blank=True)
    adjective = models.CharField(max_length=50, blank=True)
    adverb = models.CharField(max_length=50, blank=True)
    verb = models.CharField(max_length=50, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return f'{self.noun} | {self.adjective} | {self.adverb} | {self.verb}'


