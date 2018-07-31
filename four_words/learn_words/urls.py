from django.urls import path

from .views import four_words_page, word_page

urlpatterns = [
    path('four-words/', four_words_page, name='four-words'),
    path('<int:word_id>/', word_page, name='word-info')
]
