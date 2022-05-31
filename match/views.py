from ast import match_case
from django.shortcuts import render, redirect
from django.contrib import messages

from menu.models import Cocktail


def match(request):
    """ A view to return the cocktail match main page """
    
    answers_list = [
        ['match_wine','match_beer', 'match_cocktail'],
        ['match_dry', 'match_sweet'], 
        ['match_single', 'match_double'],
        ['match_hard', 'match_calm'], 
        ['match_romantic', 'match_work', 'match_party'], 
        ['match_vodka', 'match_rum', 'match_tequilla'], 
        ['match_no_letter', 'match_yes_letter'], 
        ['match_yes_working', 'match_no_working'], 
        ['match_yes_enjoy', 'match_no_enjoy']
    ]
    
    if request.method == 'POST':
        data_list = request.POST
        
        # Validate the forms and data
        for i in data_list:
            if i == 'csrfmiddlewaretoken':
                continue
            if i not in (item for sublist in answers_list for item in sublist):
                messages.add_message(
                    request, messages.ERROR, 'We found an error in the form. Try again!', extra_tags='alert')
                return redirect('match')
        for answer in answers_list:
            if not any(data in data_list for data in answer):
                messages.add_message(
                    request, messages.ERROR, 'We found an error in the form. Try again!', extra_tags='alert')
                return redirect('match')
        
        result = Cocktail.objects.all()
        
        return redirect('match_result', result)
            
    return render(request, 'match/index.html')


def match_result(request, result):
    """ A view to return the result of the match """
    
    print(result[0].name)
    
    return render(request, 'match/index.html')