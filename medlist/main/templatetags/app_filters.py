from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter(name='translate')
def translate(obj, lang):
    return obj.get_translation(lang)

@register.simple_tag
def field_lang(obj, field_name, lang):
    lang_code = lang[0:2]
    field_value = None
    field_name_translate = "%s_%s" % (field_name,lang_code)

    field_value = getattr(obj, field_name_translate, "")

    # if not have translation content for the field get default field value
    if not field_value:        
        field_value = getattr(obj, field_name)

    return mark_safe(field_value)