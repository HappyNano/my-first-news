from django import template

register = template.Library()

@register.filter(name='split')
def split(value, arg):
    return value.split(arg)
	
register.filter('split', split)

import re
from django.utils.safestring import mark_safe

@register.filter
def add_class(field, class_name):
    return field.as_widget(attrs={
        "class": " ".join((field.css_classes(), class_name))
    })