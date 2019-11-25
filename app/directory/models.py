#! coding: utf-8
import os
from django.db import models
from datetime import datetime
from medlist import settings
from django.utils.translation import ugettext_lazy as _
from django.template.defaultfilters import slugify
from django.db.models.functions import Lower

LANGUAGES_CHOICES = (
    ('en', 'English'),    # default language
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
)

class Medicine(models.Model):

    class Meta:
        ordering = [Lower('name'), ]


    name = models.CharField(max_length=255)
    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)
    active = models.BooleanField(_("active"), default=True)

    def __unicode__(self):
        return str(self.name)

    def get_link(self):
        return reverse('medlist.directory.views.show_medicine', kwargs={'id': self.id})

    def get_translation(self, lang_code):
        translation = MedicineLocal.objects.filter(medicine=self.id, language=lang_code)
        if translation:
            return translation[0].name
        else:
            return self.name

    def __str__(self):
        return str(self.name)

class MedicineLocal(models.Model):

    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"

    medicine = models.ForeignKey(Medicine, verbose_name=_("medicine"), on_delete=models.CASCADE)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES[1:])
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return str(self.name)


class PharmaceuticalFormType(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form Type"
        verbose_name_plural = "Pharmaceutical Form Types"
        ordering = [Lower('name'), ]

    name = models.CharField(_("name"), max_length=255)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

    def get_translation(self, lang_code):
        translation = PharmaceuticalFormTypeLocal.objects.filter(pharmaceutical_form_type=self.id, language=lang_code)
        if translation:
            return translation[0].name
        else:
            return self.name

    def get_translations(self):
        translation_list = ["en^%s" % self.name.strip()]
        translation = PharmaceuticalFormTypeLocal.objects.filter(pharmaceutical_form_type=self.id)
        if translation:
            other_languages = ["%s^%s" % (trans.language, trans.name.strip()) for trans in translation]
            translation_list.extend(other_languages)

        return translation_list

    def __str__(self):
        return self.name

class PharmaceuticalFormTypeLocal(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form Type Translation"
        verbose_name_plural = "Pharmaceutical Form Type Translations"
        ordering = [Lower('name'), ]

    pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType, on_delete=models.CASCADE)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES[1:])
    name = models.CharField(_("name"), max_length=255)

    def __str__(self):
        return self.name


class PharmaceuticalForm(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form"
        verbose_name_plural = "Pharmaceutical Forms"
        ordering = [Lower('medicine__name'), ]

    medicine = models.ForeignKey(Medicine, verbose_name=_("medicine"), on_delete=models.CASCADE)
    pharmaceutical_form_type =  models.ForeignKey(PharmaceuticalFormType, verbose_name=_("pharmaceutical form type"), on_delete=models.CASCADE)
    atc_code = models.CharField(_("atc code"), max_length=255, blank=True)
    composition = models.CharField(_("composition"), max_length=255, blank=True)
    composition_es = models.CharField(_("composition (Spanish)"), max_length=255, blank=True)
    composition_pt = models.CharField(_("composition (Portuguese)"), max_length=255, blank=True)
    active = models.BooleanField(_("active"), default=True)

    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)

    def medicine_id(self):
        return str(self.medicine.id)

    def __str__(self):
        output = "%s - %s" % (self.medicine, self.pharmaceutical_form_type)
        if self.composition:
            output += "%s" % (self.composition)

        return str(output)
