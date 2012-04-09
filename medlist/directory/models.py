#! coding: utf-8
import os
from django.db import models
from datetime import datetime
from medlist import settings
from django.utils.translation import ugettext_lazy as _

LANGUAGES_CHOICES = (
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
)  

class Medicine(models.Model):

    name = models.CharField(max_length=255)
    
    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)
    active = models.BooleanField(_("active"), default=True)
    
    def __unicode__(self):
        return unicode(self.name)

    def get_link(self):
        return reverse('medlist.directory.views.show_medicine', kwargs={'id': self.id})

    def get_translation(self, lang_code):
        translation = MedicineLocal.objects.filter(medicine=self.id, language=lang_code)
        if translation:
            return translation[0].name
        else:
            return self.name

    def __unicode__(self):
        return unicode(self.name)

class MedicineLocal(models.Model):

    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"

    medicine = models.ForeignKey(Medicine, verbose_name=_("medicine"))
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)
    
    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"

class EvidenceSummary(models.Model):

    class Meta:
        verbose_name = "Medicine Evidence Summary"
        verbose_name_plural = "Medicine Evidence Summaries"

    medicine = models.ForeignKey(Medicine, verbose_name=_("medicine"))
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    context = models.TextField(_("context"))
    question = models.TextField(_("question"))
    link = models.TextField(_("link"), blank=True)
    file = models.FileField(_("file"), upload_to='evidences_files', blank=True)
    
    class Meta:
        verbose_name = "Medicine Evidence Summary"
        verbose_name_plural = "Medicine Evidence Summaries"

    def __unicode__(self):
        return unicode(self.context)

class PharmaceuticalFormType(models.Model):    

    class Meta:
        verbose_name = "Pharmaceutical Form Type"
        verbose_name_plural = "Pharmaceutical Form Types"

    name = models.CharField(_("name"), max_length=255)
    
    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)   

    def __unicode__(self):
        return unicode(self.name)

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


    def __unicode__(self):
        return unicode(self.name)

class PharmaceuticalFormTypeLocal(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form Type Translation"
        verbose_name_plural = "Pharmaceutical Form Type Translations"

    pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType)
    language = models.CharField(_("language"), max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(_("name"), max_length=255)

class PharmaceuticalForm(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form"
        verbose_name_plural = "Pharmaceutical Forms"

    medicine = models.ForeignKey(Medicine, verbose_name=_("medicine"))
    pharmaceutical_form_type =  models.ForeignKey(PharmaceuticalFormType, verbose_name=_("pharmaceutical form type"))
    atc_code = models.CharField(_("atc code"), max_length=255, blank=True)
    composition = models.CharField(_("composition"), max_length=255, blank=True)
    active = models.BooleanField(_("active"), default=True)
    
    created = models.DateTimeField(_("date creation"), default=datetime.now, editable=False)
    
    def medicine_id(self):
        return unicode(self.medicine.id)

    def __unicode__(self):
        output = "%s - %s" % (self.medicine, self.pharmaceutical_form_type)
        if self.composition:
            output += "%s" % (self.composition)

        return unicode(output)