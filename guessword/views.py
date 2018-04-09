# Stdlib imports
# Core Django imports
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
# Third-party app imports
# Imports from your apps
from .models import WordsModel

GAME_OVER_MSG = "Your chances have expired"
WINNER_MSG = "You have guessed the word!!!"

CHANCES = 7
WORD_IS_GUESSED = -1
LETTER_IS_NOT_IN_WORD = -2
YOUR_CHANCES_HAVE_EXPIRED = None


def initialize_session(request):
    request.session['chances'] = CHANCES
    current_word = WordsModel.words.random()
    current_word = str(current_word)
    word_letters = list(enumerate(current_word))
    request.session['word_letters'] = word_letters
    return len(current_word)


def clear_session(request):
    request.session.flush()


class GuessWordView(View):
    template_name = 'game.html'

    @staticmethod
    def check_if_letter_is_in_word(request, letter):

        matched_indexes = []
        for idx, item in enumerate(request.session['word_letters']):
            if letter == item[1]:
                matched_indexes.append(item[0])
                request.session['word_letters'].pop(idx)

        if not request.session['word_letters']:
            clear_session(request)
            messages.add_message(request, messages.SUCCESS, WINNER_MSG)
            return render(request, 'game.html')

        if matched_indexes:
            return JsonResponse({'failed': 0, 'indexes': matched_indexes})

        request.session['chances'] -= 1
        if not request.session['chances']:
            clear_session(request)
            messages.add_message(request, messages.INFO, GAME_OVER_MSG)
            return render(request, 'game.html')
        return JsonResponse({'failed': 1})

    def get(self, request):
        clear_session(request)
        count = initialize_session(request)
        context = {'letters_count': list(range(count))}
        return render(request, self.template_name, context=context)

    def post(self, request):
        letter = request.POST.get('letter')
        response = self.check_if_letter_is_in_word(request, letter)
        return response
