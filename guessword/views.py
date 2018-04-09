# Stdlib imports
# Core Django imports
from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
# Third-party app imports
# Imports from your apps
from .models import WordsModel

CHANCES = 7
WORD_IS_GUESSED = -1
LETTER_IS_NOT_IN_WORD = -2
YOUR_CHANCES_HAVE_EXPIRED = None


class GuessWordView(View):
    template_name = 'game.html'

    @staticmethod
    def check_if_letter_in_word(request, letter):
        if not request.session['chances']:
            return YOUR_CHANCES_HAVE_EXPIRED

        if not request.session['word_letters']:
            return WORD_IS_GUESSED

        matched_indexes = []
        for idx, item in enumerate(request.session['word_letters']):
            if letter == item[1]:
                matched_indexes.append(item[0])
                request.session['word_letters'].pop(idx)

        if matched_indexes:
            return matched_indexes

        request.session['chances'] -= 1
        return LETTER_IS_NOT_IN_WORD

    @staticmethod
    def clear_session(request):
        request.session.flush()

    @staticmethod
    def initialize_session(request):
        request.session['chances'] = CHANCES
        current_word = WordsModel.words.random()
        current_word = str(current_word)
        word_letters = list(enumerate(current_word))
        request.session['word_letters'] = word_letters
        return len(current_word)

    def get(self, request):
        self.clear_session(request)
        count = self.initialize_session(request)
        context = {'letters_count': list(range(count))}
        return render(request, self.template_name, context=context)

    def post(self, request):
        letter = request.POST.get('letter')
        status = self.check_if_letter_in_word(request, letter)

        if status == YOUR_CHANCES_HAVE_EXPIRED:
            self.clear_session(request)
            messages.add_message(request, messages.ERROR, "Your chances have expired")
            return render(request, 'results.html')

        elif status == WORD_IS_GUESSED:
            self.clear_session(request)
            messages.add_message(request, messages.SUCCESS, "You have guessed the word!!!")
            return render(request, 'results.html')

        elif status == LETTER_IS_NOT_IN_WORD:
            return JsonResponse({'failed': 1})
        else:
            return JsonResponse({'failed': 0, 'indexes': status})
