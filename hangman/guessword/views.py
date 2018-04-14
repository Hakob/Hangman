from django.views import View
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from .utils import initialize_session, clear_session, is_letter_exists, update_dash, is_end


def initpage(request):
    return render(request, 'index.html')


class GuessWordView(View):
    template_name = 'end.html'

    def post(self, request):
        letter = request.POST.get('letter', '')
        is_letter_exists(request, letter)
        if is_end(request):
            template = loader.get_template(self.template_name)
            rendered = template.render()
            return HttpResponse(rendered)
        new_dash = update_dash(request)
        return HttpResponse(new_dash)


class StartPageView(View):
    template_name = 'game.html'

    def get(self, request):
        clear_session(request)
        initialize_session(request)
        context = {'guessed_letters': request.session['guessed_letters']}
        return render(request, self.template_name, context=context)
