from django.contrib import admin
from .models import Booking

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'booking_name',
        'booking_date',
        'booking_time',
        'booking_size',
        'booking_email',
    )
    
    ordering = ('booking_date',)


admin.site.register(Booking, ProductAdmin)