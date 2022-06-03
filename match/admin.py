from django.contrib import admin
from .models import *

# Register your models here.

class EnjoyCheckMaltAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'enjoy',
        'non_enjoy',
    )


admin.site.register(MatchingQuestions)
admin.site.register(EnjoyCheckMalt, EnjoyCheckMaltAdmin)