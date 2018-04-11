from .models import WordsModel

CHANCES = 7


def initialize_session(request):
    request.session['chances'] = CHANCES
    current_word = WordsModel.words.random()
    current_word = str(current_word)
    word_letters = list(enumerate(current_word))
    request.session['word_letters'] = word_letters


def clear_session(request):
    request.session.flush()
