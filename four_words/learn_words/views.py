from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from .models import FourWords
# from .forms import AddNewWord

from django.views.generic import View

from django.contrib.auth.models import User

def four_words_page(request):
    search = request.GET.get('search', '')
    four_words = FourWords.objects.filter(noun__contains=search)
    return render(request, 'four_words.html', {'four_words': four_words})


def word_page(request, word_id):
    word = get_object_or_404(FourWords, id=word_id)
    return render(request, 'word_info.html', {'word': word})


class AddWord(View):

    def get(self, request):
        return render(request, 'add_word.html', {'form': AddNewWord})

    def post(self, request):
        form = AddNewWord(request.POST)
        if form.is_valid():
            word_form = form.save(commit=False)
            word_form.save()
            return redirect('four-words')
        return render(request, 'add_word.html', {'form': form})


def user_words(request, user_id):
    user = get_object_or_404(User, id=user_id)
    words = FourWords.objects.filter(author=user)
    return render(request, 'user-words.html', {'words': words})
