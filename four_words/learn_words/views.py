from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404

from .models import FourWords


def four_words_page(request):
    four_words = FourWords.objects.all()
    return render(request, 'four_words.html', {'four_words': four_words})


def word_page(request, word_id):
    word = get_object_or_404(FourWords, id=word_id)
    return render(request, 'word_info.html', {'word': word})
