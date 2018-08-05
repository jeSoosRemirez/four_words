from django.urls import path

from .views import four_words_page, word_page,user_words

urlpatterns = [
    # path('add-new-word/', AddNewWord, name='add_new_word'),
    path('four-words/', four_words_page, name='four-words'),
    path('word/<int:word_id>/', word_page, name='word-info'),
    path('user/<int:user_id>/', user_words, name='user-words')
]
