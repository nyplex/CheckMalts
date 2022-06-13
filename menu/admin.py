from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

class SubCategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

class CocktailSizeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'sizes',
    )

class CocktailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'has_size',
        'category',
        'sub_category',
        'allow_match',
        'out_of_stock'
    )
    list_editable=['out_of_stock', 'allow_match']


admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CocktailsSize, CocktailSizeAdmin)