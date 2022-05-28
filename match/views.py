from django.shortcuts import render


def match(request):
    """ A view to return the cocktail match main page """

    return render(request, 'match/index.html')