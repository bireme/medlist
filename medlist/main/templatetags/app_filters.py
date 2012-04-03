from django import template

register = template.Library()

@register.filter(name='translate')
def translate(obj, lang):
    return obj.get_translation(lang)