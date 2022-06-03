from ast import match_case
from django.shortcuts import render, redirect
from django.contrib import messages
from .utils import match_calcul

from menu.models import Cocktail


def match(request):
    """ A view to return the cocktail match main page """

    answers_list = [
        ['wine', 'beer', 'cocktail'],
        ['dry', 'sweet'],
        ['single', 'double'],
        ['hard', 'calm'],
        ['romantic', 'after_work', 'party'],
        ['vodka', 'rum', 'tequilla'],
        ['working_tomorrow', 'no_working_tomorrow'],
        ['enjoy', 'no_enjoy']
    ]
    data_match = []

    if request.method == 'POST':
        data_list = request.POST

        # Validate the forms and data
        for answer in answers_list:
            if not any(data in data_list for data in answer):
                messages.add_message(
                    request, messages.ERROR, 'We found an error in the form. Try again!', extra_tags='alert')
                return redirect('match')

        for data in data_list:
            if data == 'no_working_tomorrow' or data == 'csrfmiddlewaretoken':
                continue
            if data == 'no_enjoy' or data == 'enjoy':
                # save enjoy data in DB
                continue
            data_match.append(data)
        match_calcul(request, data_match)

        return redirect('match_result')

    return render(request, 'match/index.html')


def match_result(request):
    """ A view to return the result of the match """

    result = request.session.get('match_result')
    questions = 7
    cocktails = []
    for key in result:
        percentage = 100 - (round(abs((result[key] - questions) / ((result[key] + questions) / 2) * 100) / 10) * 10)
        if percentage <= 10 and percentage >= -10:
            percentage = 10
        if percentage <= -10:
            percentage = 0

        cocktail = Cocktail.objects.get(pk=key)
        cocktails.append([cocktail, percentage])

    context = {
        'cocktails': cocktails
    }

    return render(request, 'match/match_result.html', context=context)
7