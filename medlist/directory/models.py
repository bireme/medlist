#! coding: utf-8
from django.db import models
from datetime import datetime

PHARMACEUTICAL_FORM_TYPE = (
    ('INJ', 'Injection'),
    ('COMP', 'Comprimido'),
    ('TAB', 'Tablet'),
)

class Language(models.Model):
    class Meta:
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'

    def __unicode__(self):
        return unicode(self.abbreviation)

    abbreviation = models.CharField(max_length=10)
    name = models.CharField(max_length=255)    


class MedicineList(models.Model):
    abbreviation = models.CharField(max_length=20)
    name = models.CharField(max_length=255)    
    
    def __unicode__(self): 
        return unicode(self.abbreviation)    


class Medicine(models.Model):
    id = models.AutoField(primary_key=True)
    def __unicode__(self):
        translations = MedicineLocal.objects.filter(medicine=self.id)
        if len(translations) > 0:
            return translations[0].name
        else:
            return unicode('(No Labels)')    


# Tabela com itens traduzidos do Model Medicine
class MedicineLocal(models.Model):
    medicine = models.ForeignKey(Medicine)
    language = models.ForeignKey(Language)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"


class PharmaceuticalForm(models.Model):
    medicine = models.ForeignKey(Medicine)
    medicineList = models.ManyToManyField(MedicineList)
    pharmaceutical_form_type = models.CharField(max_length=50, choices=PHARMACEUTICAL_FORM_TYPE)
    atc_code = models.CharField(max_length=255)
    coposition = models.CharField(max_length=255)

    def medicine_id(self):
        return unicode(self.medicine.id)

    def __unicode__(self):
        return unicode(self.pharmaceutical_form_type)