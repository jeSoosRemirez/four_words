
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views.generic import View
from django.contrib.auth.models import User

from .models import FourWords
from .forms import AddNewWord, EditFourWords



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
            word_type = form.cleaned_data['word_type']

            author_id = request.user.id
            pub_date = timezone.now()
            if word_type == '1':
                four_words = FourWords(
                    author_id=author_id,
                    pub_date=pub_date,
                    noun=word,
                )
                four_words.save()
                return redirect('word-info', word_id=four_words.pk)
            elif word_type == '2':
                four_words = FourWords(
                    author_id=author_id,
                    pub_date=pub_date,
                    adjective=word,
                )
                four_words.save()
                return redirect('word-info', word_id=four_words.pk)
            elif word_type == '3':
                four_words = FourWords(
                    author_id=author_id,
                    pub_date=pub_date,
                    adverb=word,
                )
                four_words.save()
                return redirect('word-info', word_id=four_words.pk)
            elif word_type == '4':
                four_words = FourWords(
                    author_id=author_id,
                    pub_date=pub_date,
                    verb=word,
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

