from django.contrib import admin
from .models import *

# Register your models here.

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

class CocktailAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
        'has_size',
        'category',
        'sub_category',
        'allow_match',
    )

class IngredientAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'friendly_name',
    )

class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__'
    )

admin.site.register(Ingredient, IngredientAdmin)
admin.site.register(Cocktail, CocktailAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(CocktailsSize)