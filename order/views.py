from django.shortcuts import render
from django.template.loader import render_to_string
from django.contrib import messages
from menu.models import *
from django.http import HttpResponse


# Create your views here.


def order(request):
    
    categories = Category.objects.all()
    
    if not Category.objects.filter(pk=request.GET.get('category')).exists() or request.GET.get('category') is None :
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
    if request.method == "POST":
        # get the form data
        cocktail = Cocktail.objects.get(pk=request.POST['item_id'])


    html = render_to_string('order/includes/item_modal.html', {'cocktail': cocktail})
    return HttpResponse(html)