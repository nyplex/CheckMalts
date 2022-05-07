from django.shortcuts import render
from allauth.account.decorators import login_required


@login_required()
def checkout(request):
    """ A view to render the order page """


    return render(request, 'home/home.html')