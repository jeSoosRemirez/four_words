
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.models import User

from .models import FourWords
from .forms import AddNewWord, EditFourWords

import requests
import json
from django.conf import settings

from googletrans import Translator

from django.views.generic.base import View


class AddWord(View):

    def get(self, request):
        return render(request, 'base.html', {'form': AddNewWord})

    def post(self, request):
        form = AddNewWord(request.POST)
        if form.is_valid():
            word_form = form.save(commit=False)
            word_form.save()
            return redirect('four-words')
        return render(request, 'base.html', {'form': form})

def four_words_page(request):
    search = request.GET.get('search', '')
    four_words = FourWords.objects.filter(noun__contains=search)
    return render(request, 'four_words.html', {'four_words': four_words})


def word_page(request, word_id):
    word = get_object_or_404(FourWords, id=word_id)
    return render(request, 'word_info.html', {'word': word})

def user_words(request, user_id):
    user = get_object_or_404(User, id=user_id)
    words = FourWords.objects.filter(author=user)
    return render(request, 'user-words.html', {'words': words})

def new_word(request):
    if request.method == "POST":
        form = AddNewWord(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']

            translator = Translator()
            translate = translator.translate(word, dest='uk')
            translates = translate.text
            author_id = request.user.id
            pub_date = timezone.now()
            url = 'https://od-api.oxforddictionaries.com:443/api/v1/entries/en/{}'.format(word.lower())
            r = requests.get(url, headers={'app_id': settings.OXFORD_APP_ID, 'app_key': settings.OXFORD_APP_KEY})
            if r.status_code == 200:
                response = r.json()
                result = response['results'][0]['lexicalEntries'][0]
                word_type = result['lexicalCategory']
                description = result['entries'][0]['senses'][0].get('definitions') if not None else ''
                word_description = description[0] if description else ''
                examples = result['entries'][0]['senses'][0].get('examples') if not None else ''
                word_example = examples[0]['text'] if examples else ''
                if word_type == 'Noun':
                    four_words = FourWords(
                        author_id=author_id,
                        pub_date=pub_date,
                        noun=word,
                        noun_description=word_description,
                        noun_example=word_example,
                        noun_translate=translates,
                    )
                    four_words.save()
                    return redirect('word-info', word_id=four_words.pk)
                elif word_type == 'Adjective':
                    four_words = FourWords(
                        author_id=author_id,
                        pub_date=pub_date,
                        adjective=word,
                        adjective_description=word_description,
                        adjective_example=word_example,
                        adjective_translate=translates,
                    )
                    four_words.save()
                    return redirect('word-info', word_id=four_words.pk)
                elif word_type == 'Adverb':
                    four_words = FourWords(
                        author_id=author_id,
                        pub_date=pub_date,
                        adverb=word,
                        adverb_description=word_description,
                        adverb_example=word_example,
                        adverb_translate=translates,
                    )
                    four_words.save()
                    return redirect('word-info', word_id=four_words.pk)
                elif word_type == 'Verb':
                    four_words = FourWords(
                        author_id=author_id,
                        pub_date=pub_date,
                        verb=word,
                        verb_description=word_description,
                        verb_example=word_example,
                        verb_translate=translates,
                    )
                    four_words.save()
                    return redirect('word-info', word_id=four_words.pk)
                else:
                    four_words = FourWords(
                        author_id=author_id,
                        pub_date=pub_date,
                        other=word,
                        other_description=word_description,
                        other_example=word_example,
                        other_translate=translates,
                    )
                    four_words.save()
                    return redirect('word-info', word_id=four_words.pk)
            else:
                four_words = FourWords(
                    author_id=author_id,
                    pub_date=pub_date,
                    other=word,
                )
                four_words.save()
                return redirect('word-info', word_id=four_words.pk)

    else:
        form = AddNewWord()
    return render(request, 'edit_word.html', {'form': form})

def edit_four_words(request, word_id):
    four_words = get_object_or_404(FourWords, pk=word_id)
    if request.method == "POST":
        form = EditFourWords(request.POST, instance=four_words)
        if form.is_valid():
            four_words = form.save(commit=False)
            four_words.author_id = request.user
            four_words.pub_date = timezone.now()
            four_words.save()
            return redirect('word-info', word_id=four_words.pk)
    else:
        form = EditFourWords(instance=four_words)
    return render(request, 'edit_four_words.html', {'form': form})

