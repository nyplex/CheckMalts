from django.shortcuts import render
from django.template.loader import render_to_string
from requests import Response
from menu.models import *
from django.http import Http404, HttpResponse, HttpResponseNotFound, JsonResponse
from django.middleware import csrf
from django.conf import settings



def order(request):
    """ A view to render the order page """

    categories = Category.objects.all()
    
    if request.GET.get('category') is None:
        category = 1
    elif not Category.objects.filter(pk=request.GET.get('category')).exists():
        raise Http404
    else:
        category = int(request.GET.get('category'))

    cocktails = Cocktail.objects.filter(category=category)
    sub_categories = SubCategory.objects.filter(category__id=category)

    context = {
        'open': settings.OPEN,
        'categories': categories,
        'sub_categories': sub_categories,
        'cocktails': cocktails,
        'selected': category
    }
    return render(request, 'order/order.html', context)


def item_detail(request):
    """ A view to return the item modal from the Ajax call """

    if request.method == "POST":
        try:
            cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
        except Cocktail.DoesNotExist:
            return JsonResponse({}, status=404)
        
    html = render_to_string(
        'order/includes/item_modal.html', {'cocktail': cocktail, 'csrf_token': csrf.get_token(request)})
    return HttpResponse(html)


def calculate_size_price(request):
    """ A view that return the updated price of a item 
        to the ajax call depending of its size & qty """

    if request.method == "POST":
        try:
            cocktail = Cocktail.objects.get(pk=request.POST['item_id'])
        except Cocktail.DoesNotExist:
            return JsonResponse({}, status=404)

        if cocktail.has_size == True:
            if(request.POST['size']
               and request.POST['size']
               in ['small', 'medium', 'large', 'single', 'double', 'triple']):

                size = request.POST['size']
                price = calculate_price_by_size(cocktail.price, cocktail.net_price, size)
        
            else:
                return JsonResponse({}, status=404)

        if request.POST['quantity']:
            if int(request.POST['quantity']) <= 0 or int(request.POST['quantity']) > 10:
                return JsonResponse({}, status=404)
            qty = int(request.POST['quantity'])
        else:
            qty = 1

        price = round(price * qty, 1)
        return JsonResponse({"response": price}, status=200)
    


def calculate_price_by_size(price, net_price, size):
    diff = price - net_price
    match size:
        case 'small' | 'single':
            price = price
        case 'medium':
            price = price = round(
                (((net_price * 2) / 3) * 2) + diff, 1)
        case 'large':
            price = round((net_price * 2) + diff, 1)
        case 'double':
            price = round(price * 2, 1)
        case 'triple':
            price = round(price * 3, 1)
        case _:
            raise Http404
    
    return price
