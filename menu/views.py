from django.shortcuts import render
from .models import *
from django.http import JsonResponse
from django.core import serializers

def menu(request):
    """ A view to return the menu page """
    
    cocktail = Cocktail.objects.get(pk=1)

    context = {
        'cocktail': cocktail
    }
    
    return render(request, 'menu/menu.html', context)


def admin(request):
    
    cocktails = Cocktail.objects.all()
    ingredients = Ingredient.objects.all().order_by('category')
    
    context = {
        'cocktails': cocktails,
        'ingredients': ingredients
    }
    
    return render(request, 'menu/admin.html', context)


def postRecipe(request):
    # request should be ajax and method should be POST.
    if request.method == "POST":
        # get the form data
        cocktail = Cocktail.objects.get(pk=request.POST['cocktail'])
        ingredient = Ingredient.objects.get(pk=request.POST['ingredient'])
        quantity = request.POST['quantity']
        recipe = Recipe(ingredient=ingredient, cocktail=cocktail, quantity=quantity)
        recipe.save()

    # some error occured
    return JsonResponse({"error": ""}, status=400)