from django.shortcuts import render


def menu(request):
    """ A view to return the menu page """

    
    return render(request, 'products/menu.html')