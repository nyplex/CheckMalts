from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from menu.models import *
from django.http import HttpResponse, JsonResponse, Http404
import math


# Create your views here.


def order(request):
    """ A view to render the order page """

    categories = Category.objects.all()

    if not Category.objects.filter(pk=request.GET.get('category')).exists() or request.GET.get('category') is None:
        category = 1
    else:
        category = int(request.GET.get('category'))
        
    cocktails = Cocktail.objects.filter(category=category)
    sub_categories = SubCategory.objects.filter(category__id=category)

    context = {
        'open': True,
        'categories': categories,
        'sub_categories': sub_categories,
        'cocktails': cocktails,
        'selected': category
    }

    return render(request, 'order/order.html', context)


def item_detail(request):
    """ A view to return the item modal from the Ajax call """

    if request.method == "POST":
        # get the form data
        cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
        
    html = render_to_string(
        'order/includes/item_modal.html', {'cocktail': cocktail})
    return HttpResponse(html)


def calculate_size_price(request):
    """ A view that return the updated price of a item to the ajax call depending of its size & qty """

    if request.method == "POST":
        
        try:
            cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
            net_price = cocktail.net_price
            diff = cocktail.price - net_price
            price = cocktail.price
            
        except Cocktail.DoesNotExist:
            print('first error')
            return JsonResponse({}, status=404)
        
        
        if cocktail.has_size == True:
            if(request.POST['size'] 
               and request.POST['size'] 
               in ['small', 'medium', 'large', 'single', 'double', 'triple']):
                
                size = request.POST['size']
                match size:
                    case 'small' | 'single':
                        price = price
                    case 'medium':
                        price =  price = round((((net_price * 2) / 3) * 2) + diff, 1)
                    case 'large':
                        price = round((net_price * 2) + diff, 1)
                    case 'double':
                        price = round(price * 2, 1)
                    case 'triple':
                        price = round(price * 3, 1)
                    case _:
                        print('second error')
                        return JsonResponse({}, status=404)
            else:
                print('error here')
                return JsonResponse({}, status=404)
        
        if request.POST['quantity']:
            qty = int(request.POST['quantity'])
        else:
            qty = 1
            
        price = round(price * qty, 1)
        return JsonResponse({"response": price}, status=200)        
            
        
