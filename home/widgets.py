from random import choices
from django.forms.widgets import Select
from django.utils.translation import gettext_lazy as _


class SelectCustomWidget(Select):
    
    def __init__(self, attrs=None, choices=(), disabled_choices=()):
        super(Select, self).__init__(attrs, choices=choices)
        self.attrs = {'class': 'primary-select-input'}

    def create_option(self, *args,**kwargs):
        option = super().create_option(*args,**kwargs)
        if not option.get('value'):
            option['attrs']['disabled'] = 'disabled'

        return option
    
        

