from django.views import View
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages

from .utils import initialize_session, clear_session, is_letter_exists
from .utils import YOUR_CHANCES_HAVE_EXPIRED, WORD_IS_GUESSED, LETTER_IS_NOT_IN_WORD, MATCHED


def initpage(request):
    return render(request, 'index.html')


class GuessWordView(View):
    template_name = 'end.html'

    def get(self, request):
        letter = request.GET.get('letter', '')
        if not letter.isalpha():
            return

        is_letter_exists(request, letter)
        if request.session['state'] == LETTER_IS_NOT_IN_WORD:
            return JsonResponse({'failed': 1})

        elif request.session['state'] == MATCHED:
            response = JsonResponse(
                {'failed': 0,
                 'indexes': request.session['matched_indexes']}
            )
            return response

        elif request.session['state'] == WORD_IS_GUESSED:
            clear_session(request)
            messages.add_message(request, WORD_IS_GUESSED, "You have guessed the word!!!")
            return render(request, self.template_name)

        elif request.session['state'] == YOUR_CHANCES_HAVE_EXPIRED:
            clear_session(request)
            messages.add_message(request, YOUR_CHANCES_HAVE_EXPIRED, "Your chances have expired")
            return render(request, self.template_name)


class StartPageView(View):
    template_name = 'game.html'

    def get(self, request):
        clear_session(request)
        initialize_session(request)
        count = len(request.session['word_letters'])
        count_range = list(range(count))
        context = {'count_range': count_range}
        return render(request, self.template_name, context=context)
