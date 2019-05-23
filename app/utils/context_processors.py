#! coding: utf-8
from django.conf import settings

def django_settings(request):
    """
    Adds the settings specified in settings.TEMPLATE_VISIBLE_SETTINGS to
    the request context.
    """
    template_settings = {}

    for attr in getattr(settings, "TEMPLATE_VISIBLE_SETTINGS", ()):
        try:
            template_settings[attr] = getattr(settings, attr)
        except AttributeError:
            m = "TEMPLATE_VISIBLE_SETTINGS: '{0}' does not exist".format(attr)
            raise ImproperlyConfigured(m);

    return template_settings
