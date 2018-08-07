from django.http import HttpResponse

from django.shortcuts import render, get_object_or_404, redirect

from .models import FourWords

from django.views.generic import View

from django.contrib.auth.models import User

class AddWord(View):

    def get(self, request):
        return render(request, 'base.html', {'form': AddNewWord})

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
