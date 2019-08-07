#! coding: utf-8
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey

from directory.models import PharmaceuticalForm


LANGUAGES_CHOICES = (
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
    ('en', 'English'),
)

class List(models.Model):

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
        verbose_name = _("list")
        verbose_name_plural = _("lists")

    name = models.CharField(_("name"), max_length=255)
    abbreviation = models.CharField(_("abbreviation"), max_length=50)
    year = models.IntegerField(_("year of publication"))
    edition = models.CharField(_("edition"), max_length=50, blank=True)
    type = models.CharField(_("Type"), max_length=1, choices=LIST_TYPES)
    subtype = models.CharField(_("sub-Type"), max_length=1, choices=LIST_SUBTYPES, null=True, blank=True)
    published = models.BooleanField(_("published"), default=False)
    obs = models.TextField(_("observation"), null=True, blank=True)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

    def get_translation(self, lang_code):
        attr = None
        if "|" in lang_code:
            lang_code = lang_code.split("|")
            attr = lang_code[1]
            lang_code = lang_code[0]

        translations = ListLocal.objects.filter(list=self.id, language=lang_code)

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


    def get_translations(self):
        translation_list = ["en^%s" % self.name.strip()]
        translation = ListLocal.objects.filter(list=self.id)
        if translation:
            other_languages = ["%s^%s" % (trans.language, trans.name.strip()) for trans in translation]
            translation_list.extend(other_languages)

        return translation_list

    def __str__(self):
        return str(self.name)

class ListLocal(models.Model):

    list = models.ForeignKey(List, verbose_name=_("list"), on_delete=models.PROTECT)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)
    obs = models.TextField(_("observation"), null=True, blank=True)

    class Meta:
        verbose_name = "List Translation"
        verbose_name_plural = "List Translations"

    def __str__(self):
        return str(self.language)


class Section(MPTTModel):

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(_("title"), max_length=255)
    parent = TreeForeignKey('Section', verbose_name=_("parent section"), blank=True, null=True, related_name='children', on_delete=models.PROTECT)
    list = models.ForeignKey(List, verbose_name=_("list"), on_delete=models.PROTECT)
    observation = models.TextField(_("observation"), blank=True, null=True)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

    def get_parent_title(self):
        if self.parent:
            return str(self.parent.title)

    def get_clean_title(self):
        return self.clean_title(self.title)

    def get_list_abbreviation(self):
        return str(self.list.abbreviation)

    def get_hierarchy(self):
        hierarchy_list = [sec.title for sec in self.get_ancestors()]
        hierarchy_list.append(self.title)
        hierarchy_flat = "/ ".join(hierarchy_list)

        return hierarchy_flat

    def get_translation(self, lang_code):

        attr = None
        if "|" in lang_code:
            lang_code = lang_code.split("|")
            attr = lang_code[1]
            lang_code = lang_code[0]

        translations = SectionLocal.objects.filter(section=self.id, language=lang_code)

        if translations:
            translation = translations[0]
            if attr:
                if hasattr(translation, attr):
                    return getattr(translation, attr)
            else:
                return translation.title

        if not translations:
            if attr:
                return getattr(self, attr)

        return self.title


    def get_translations(self):
        translation_list = ["en^%s" % self.clean_title(self.title)]
        translation = SectionLocal.objects.filter(section=self.id)
        if translation:
            other_languages = ["%s^%s" % (trans.language, self.clean_title(trans.title)) for trans in translation]
            translation_list.extend(other_languages)

        return translation_list

    def clean_title(self, raw_title):
        """Normalize section title removing section number, etc. Ex. 13.3. Medicines used in bipolar disorders """
        title_parts = raw_title.split('.')
        clean_title = title_parts[len(title_parts)-1]
        if (clean_title == ''):
            clean_title = title_parts[len(title_parts)-2]

        return clean_title.strip()

    def __str__(self):
        return  self.title


    get_hierarchy.short_description = _("hierarchy")

    get_list_abbreviation.short_description = _("list abbreviation")


class SectionLocal(models.Model):

    section = models.ForeignKey(Section, verbose_name=_("section"), on_delete=models.PROTECT)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    title = models.CharField(_("name"), max_length=255, null=True)
    observation = models.TextField(_("observation"), null=True, blank=True)

    class Meta:
        verbose_name = "Section Translation"
        verbose_name_plural = "Sections Translations"

    def __str__(self):
        return str(self.language)


class SectionPharmForm(models.Model):

    class Meta:
        verbose_name = _("pharmaceutical form")
        verbose_name_plural = _("pharmaceutical forms")

    section = models.ForeignKey(Section, verbose_name=_("section"), on_delete=models.PROTECT)
    pharmaceutical_form = models.ForeignKey(PharmaceuticalForm, verbose_name=_("pharmaceutical form"), on_delete=models.PROTECT)
    only_for_children = models.BooleanField(_("only for children"))
    specialist_care_for_children = models.BooleanField(_("specialist care for children"))
    observation = models.TextField(_("Observations (English)"), blank=True, null=True)
    observation_es = models.TextField(_("Observations (Spanish)"), blank=True, null=True)
    observation_pt = models.TextField(_("Observations (Portuguese)"), blank=True, null=True)
    restriction_age = models.CharField(_("Restriction age or weight (English)"), max_length=255, null=True, blank=True)
    restriction_age_es = models.CharField(_("Restriction age or weight (Spanish)"), max_length=255, null=True, blank=True)
    restriction_age_pt = models.CharField(_("Restriction age or weight (Portuguese)"), max_length=255, null=True, blank=True)
    best_evidence = models.BooleanField(_("The best evidence for effectiveness and safety"))
    complementary_list = models.BooleanField(_("complementary list"))

    def html_observation(self):
        return mark_safe(self.observation)

    def pharmaceutical_form_id(self):
        return str(self.pharmaceutical_form.id)

    def __str__(self):
        return str(self.pharmaceutical_form)
