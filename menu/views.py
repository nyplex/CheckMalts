from django.shortcuts import render
from .models import *
from django.http import JsonResponse


def menu(request, product_id=None):
    """ A view to return the menu page & product details modal """

    cocktails = Cocktail.objects.all().order_by('category')
    categories = Category.objects.all()
    subCategories = SubCategory.objects.all()

    context = {
        'cocktails': cocktails,
        'categories': categories,
        'subCategories': subCategories
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