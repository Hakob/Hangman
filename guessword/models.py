# Stdlib imports
from random import randint

# Core Django imports
from django.db import models
from django.db.models.aggregates import Count

# Third-party app imports

# Imports from your apps


class WordsManager(models.Manager):
    def random(self):
        count = self.aggregate(count=Count('id'))['count']
        random_index = randint(0, count - 1)
        return self.all()[random_index]


class WordsModel(models.Model):
    words = WordsManager()
    word = models.CharField(max_length=128, help_text='Words which need to be guessed')

    def __str__(self):
        return self.word
