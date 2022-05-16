from django.contrib import admin
from django.forms import Textarea
from .models import Order, OrderLine
from django.db import models

# Register your models here.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ('lineitem_total', 'order' ,'cocktail',
                       'cocktail_size', 'note', 'quantity')
    
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows': 5,'cols': 40})},
    }


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)

    readonly_fields = ('order_number', 'date', 'subtotal',
                       'grand_total', 'original_bag',
                       'stripe_pid', 'is_paid', 'is_cancelled', 
                       'is_pending', 'is_done', 'serivce_amount',
                       'table_number', 'user_profile')

    list_display = ('id', 'order_number', 'date',
                    'grand_total',)

    ordering = ('-date',)
    
    



admin.site.register(Order, OrderAdmin)