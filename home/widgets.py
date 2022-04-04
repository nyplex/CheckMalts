from random import choices
from django.forms.widgets import Select
from django.utils.translation import gettext_lazy as _


class SelectCustomWidget(Select):
    TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]
    choices = TITLE_CHOICES
    def create_option(self, *args,**kwargs):
        option = super().create_option(*args,**kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = 'disabled'

        return option
    
        

