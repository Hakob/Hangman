from django.urls import path

from .views import initpage, StartPageView, GuessWordView

urlpatterns = [
    path(route='',
         view=initpage,
         name='index'
         ),

    path(route='hangman/',
         view=StartPageView.as_view(),
         name='game'
         ),

    path(route='check/',
         view=GuessWordView.as_view(),
         name='check'
         ),
]
