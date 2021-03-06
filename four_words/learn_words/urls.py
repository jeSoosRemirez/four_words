from django.urls import path

from .views import four_words_page, word_page, user_words, new_word, edit_four_words, delete_word

urlpatterns = [
    # path('add-new-word/', AddNewWord, name='add_new_word'),
    path('four-words/', four_words_page, name='four-words'),
    path('word/<int:word_id>/', word_page, name='word-info'),
    path('user/<int:user_id>/', user_words, name='user-words'),
    path('four-words/<int:word_id>/edit/', edit_four_words, name='four-words-edit'),
    path('four-words/<int:word_id>/delete/', delete_word, name='four-words-delete'),
    path('four-words/new/', new_word, name='new-word'),
]
