from .models import WordsModel

CHANCES = 7
YOUR_CHANCES_HAVE_EXPIRED = 0
WORD_IS_GUESSED = -1
LETTER_IS_NOT_IN_WORD = -2
MATCHED = -3


def is_letter_exists(request, letter):
    del request.session['matched_indexes'][:]
    for idx, item in enumerate(request.session['word_letters']):
        if letter == item[1]:
            request.session['matched_indexes'].append(item[0])
            request.session['word_letters'].pop(idx)

    if not request.session['word_letters']:
        request.session['state'] = WORD_IS_GUESSED
        return
    if request.session['matched_indexes']:
        request.session['state'] = MATCHED
        return
    request.session['chances'] -= 1
    if not request.session['chances']:
        request.session['state'] = YOUR_CHANCES_HAVE_EXPIRED
        return
    request.session['state'] = LETTER_IS_NOT_IN_WORD
    return


def initialize_session(request):
    current_word = WordsModel.words.random()
    current_word = str(current_word)
    word_letters = list(enumerate(current_word))
    request.session['word_letters'] = word_letters
    request.session['matched_indexes'] = []
    request.session['chances'] = CHANCES


def clear_session(request):
    request.session.flush()
