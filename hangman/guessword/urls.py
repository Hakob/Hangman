from django.urls import path

from .views import GuessWordView

urlpatterns = [
    path(route='',
         view=GuessWordView.as_view(template_name='index.html'),
         name='index'
         ),

    path(route='hangman/',
         view=GuessWordView.as_view(template_name='game.html'),
         name='game'
         ),
]
