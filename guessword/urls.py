from django.urls import path

from .views import GuessWordView

urlpatterns = [
    path('', GuessWordView.as_view(template_name='index.html')),
    path('hangman/', GuessWordView.as_view(), name='game'),
]
