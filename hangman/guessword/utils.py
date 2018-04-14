from django.template import loader
from django.contrib import messages

from .models import WordsModel

CHANCES = 5


def is_end(request):
    if request.session['chances'] == 0:
        messages.add_message(request, messages.INFO, "Your chances have expired")
        clear_session(request)
        return True
    elif request.session['guessed_letters'] == request.session['word_letters']:
        messages.add_message(request, messages.SUCCESS, "You have guessed the word!!!")
        clear_session(request)
        return True
    return False


def update_dash(request):
    template = loader.get_template('dashboard.html')
    context = {'guessed_letters': request.session['guessed_letters']}
    rendered = template.render(context)
    return rendered


def is_letter_exists(request, letter):

    if not letter.isalpha():
        return
    count = 0
    for index, ltr in enumerate(request.session['word_letters']):
        if letter == ltr:
            request.session['guessed_letters'][index] = ltr
            count += 1
    if not count:
        request.session['chances'] -= 1


def initialize_session(request):
    current_word = WordsModel.words.random()
    current_word = str(current_word)
    request.session['word_letters'] = list(current_word)
    request.session['guessed_letters'] = list('*' * len(current_word))
    request.session['chances'] = CHANCES


def clear_session(request):
    request.session.flush()
