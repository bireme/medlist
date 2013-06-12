from django.utils.translation import ugettext_lazy as _
from django.db import models
from datetime import datetime
from list.models import *

LANGUAGES_CHOICES = (
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
    ('en', 'English'),
)

class History(models.Model):

    LIST_TYPES = (
            ('c', _('Country List')),
            ('p', _('PAHO List')),
            ('w', _('WHO List')),
        )
    LIST_SUBTYPES = (
            ('e', _('EML')),
            ('c', _('EML Children')),
            ('h', _('High Cost')),
            ('s', _('Strategic Fund')),
        )

    class Meta:
        verbose_name = _("history")
        verbose_name_plural = _("histories")

    name = models.CharField(_("name"), max_length=255)
    abbreviation = models.CharField(_("abbreviation"), max_length=50, blank=True)
    year = models.IntegerField(_("year of publication"))
    edition = models.CharField(_("edition"), max_length=50, blank=True)
    type = models.CharField(_("Type"), max_length=1, choices=LIST_TYPES)
    subtype = models.CharField(_("sub-Type"), max_length=1, choices=LIST_SUBTYPES, null=True, blank=True)
    published = models.BooleanField(_("published"), default=False)
    obs = models.TextField(_("observation"), null=True, blank=True)
    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)
    xml = models.TextField(blank=True, null=True)
    content = models.TextField()

    def get_translation(self, lang_code):
        attr = None
        if "|" in lang_code:
            lang_code = lang_code.split("|")
            attr = lang_code[1]
            lang_code = lang_code[0]

        translations = HistoryLocal.objects.filter(history=self.id, language=lang_code)
        
        if translations:
            translation = translations[0]
            if attr:
                if hasattr(translation, attr):
                    return getattr(translation, attr)
            else:
                return translation.name

        if not translations:
            if attr:
                return getattr(self, attr)
        
        return self.name


    def __unicode__(self):
        return unicode(self.name)

class HistoryLocal(models.Model):

    class Meta:
        verbose_name = _("history translation")
        verbose_name_plural = _("history translations")

    history = models.ForeignKey(History, verbose_name=_("history"), null=True)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)
    obs = models.TextField(_("observation"), null=True, blank=True)
    xml = models.TextField(blank=True, null=True)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.language)

    


