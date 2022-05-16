from django.contrib import admin
from .models import Order, OrderLine

# Register your models here.
class OrderLineAdminInline(admin.TabularInline):
    model = OrderLine
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline,)

    readonly_fields = ('order_number', 'date', 'subtotal',
                       'grand_total', 'original_bag',
                       'stripe_pid')

    list_display = ('id', 'order_number', 'date',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)