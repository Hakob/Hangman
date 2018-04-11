# Stdlib imports
# Core Django imports
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
# Third-party app imports
# Imports from your apps
from .sessions import initialize_session, clear_session

GAME_OVER_MSG = "Your chances have expired"
WINNER_MSG = "You have guessed the word!!!"

YOUR_CHANCES_HAVE_EXPIRED = 0
WORD_IS_GUESSED = -1
LETTER_IS_NOT_IN_WORD = -2


class GuessWordView(View):
    template_name = ''

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
            return WORD_IS_GUESSED

        if matched_indexes:
            return JsonResponse({'failed': 0, 'indexes': matched_indexes})

        request.session['chances'] -= 1
        if not request.session['chances']:
            clear_session(request)
            messages.add_message(request, messages.INFO, GAME_OVER_MSG)
            return YOUR_CHANCES_HAVE_EXPIRED
        return LETTER_IS_NOT_IN_WORD

    def get(self, request):
        clear_session(request)
        initialize_session(request)
        count = len(request.session['word_letters'])
        count_range = list(range(count))
        context = {'count_range': count_range}
        return render(request, self.template_name, context=context)

    def post(self, request):
        letter = request.POST.get('letter')
        state = self.check_if_letter_is_in_word(request, letter)

        if state == WORD_IS_GUESSED:
            return render(request, 'index.html')

        elif state == LETTER_IS_NOT_IN_WORD:
            return JsonResponse({'failed': 1})

        elif state == YOUR_CHANCES_HAVE_EXPIRED:
            return render(request, 'index.html')

        else:
            return state
