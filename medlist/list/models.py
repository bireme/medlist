#! coding: utf-8
from django.db import models
from medlist.directory.models import PharmaceuticalForm
from django.utils.translation import ugettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey
from datetime import datetime
from django.core.urlresolvers import reverse

LANGUAGES_CHOICES = (
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
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
    type = models.CharField(_("Type"), max_length=1, choices=LIST_TYPES)
    subtype = models.CharField(_("sub-Type"), max_length=1, choices=LIST_SUBTYPES, null=True, blank=True)
    published = models.BooleanField(_("published"), default=False)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

    def __unicode__(self):
        return unicode(self.name)

class ListLocal(models.Model):

    list = models.ForeignKey(List, verbose_name=_("list"))
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)
    
    class Meta:
        verbose_name = "List Translation"
        verbose_name_plural = "List Translations"

    def __unicode__(self):
        return unicode(self.language)


class Section(MPTTModel):

    class Meta:
        verbose_name = _("section")
        verbose_name_plural = _("sections")

    class MPTTMeta:
        order_insertion_by = ['title']

    title = models.CharField(_("title"), max_length=255)
    parent = TreeForeignKey('Section', verbose_name=_("parent section"), blank=True, null=True, related_name='children')
    list = models.ForeignKey(List, verbose_name=_("list"))
    complementary_list = models.BooleanField(_("complementary list"))
    observation = models.TextField(_("observation"), blank=True, null=True)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)
    
    def __unicode__(self):
        output = "%s - %s" % (self.list.abbreviation, self.title)
        return unicode(output)  

    def get_parent_title(self):
        if self.parent:
            return unicode(self.parent.title)

    def get_list_abbreviation(self):
        return unicode(self.list.abbreviation)  

    def get_hierarchy(self):
        hierarchy_list = [sec.title for sec in self.get_ancestors()]
        hierarchy_list.insert(0,self.title)
        hierarchy_flat = "/ ".join(hierarchy_list)

        return hierarchy_flat
    
    get_hierarchy.admin_order_field = 'parent'
    get_hierarchy.short_description = _("hierarchy")

    get_list_abbreviation.short_description = _("list abbreviation")


class SectionLocal(models.Model):

    section = models.ForeignKey(Section, verbose_name=_("section"))
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)

    class Meta:
        verbose_name = "Section Translation"
        verbose_name_plural = "Sections Translations"

    def __unicode__(self):
        return unicode(self.language)


class SectionPharmForm(models.Model):
    
    class Meta:
        verbose_name = _("pharmaceutical form")
        verbose_name_plural = _("pharmaceutical forms")

    section = models.ForeignKey(Section, verbose_name=_("section"))
    pharmaceutical_form = models.ForeignKey(PharmaceuticalForm, verbose_name=_("pharmaceutical form"))
    only_for_children = models.BooleanField(_("only for children"))
    specialist_care_for_children = models.BooleanField(_("specialist care for children"))
    observation = models.TextField(_("observation"), blank=True, null=True)
    restriction_age = models.CharField(_("restriction age or weight"), max_length=255, null=True, blank=True)

    def __unicode__(self):
        return unicode(self.pharmaceutical_form)


