from .models import MatchingQuestions
from menu.models import Cocktail


def match_calcul(request, data):
    """
    Method to calcul the match result and 
    store it into session 
    """
    
    answers = []
    ids_container = []
    duplicate_dict = {}
    
    for i in data:
        if i == 'csrfmiddlewaretoken':
            continue
        else:
            matching = MatchingQuestions.objects.get(answer=i)
            answers.append(matching)
            
    cocktails = Cocktail.objects.filter(matching_questions__in=answers, allow_match=True).order_by('pk')
    
    for cocktail in cocktails:
        ids_container.append(cocktail.id)
        
    for i in ids_container:
        duplicate_dict[i] = ids_container.count(i)
        
    marklist = sorted(duplicate_dict.items(), key=lambda x:x[1], reverse=True)
    sortdict = dict(marklist)
    result = request.session.get('match_result', {})
    result = sortdict
    
    request.session['match_result'] = result