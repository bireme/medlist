#! coding: utf-8

from django.db import models
from datetime import datetime

LANGUAGES_CHOICES = (
    ('pt-br', 'Brazilian Portuguese'),
    ('es', 'Spanish'),
)

class MedicineList(models.Model):

    class Meta:
        verbose_name = "Medicine List"
        verbose_name_plural = "Medicine Lists"

    abbreviation = models.CharField(max_length=20)
    name = models.CharField(max_length=255)    
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    
    
    def __unicode__(self): 
        return unicode(self.abbreviation)    


class Medicine(models.Model):

    name = models.CharField(max_length=255)
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    
    
    def __unicode__(self):
        return unicode(self.name)

    def creator(self):
        return self.user_creation.username


# Tabela com itens traduzidos do Model Medicine
class MedicineLocal(models.Model):

    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"

    medicine = models.ForeignKey(Medicine)
    language = models.CharField(max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(max_length=255)
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    
    
    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"


# vocabulario controlado dos tipos de Forma Farmacêutica
class PharmaceuticalFormType(models.Model):    

    class Meta:
        verbose_name = "Pharmaceutical Form Type"
        verbose_name_plural = "Pharmaceutical Form Types"

    name = models.CharField(max_length=255)
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    

    def __unicode__(self):
        return unicode(self.name)

# local do PharmaceuticalFormType
class PharmaceuticalFormTypeLocal(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form Type Translation"
        verbose_name_plural = "Pharmaceutical Form Type Translations"

    pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType)
    language = models.CharField(max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(max_length=255)
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    


class PharmaceuticalForm(models.Model):

    class Meta:
        verbose_name = "Pharmaceutical Form"
        verbose_name_plural = "Pharmaceutical Forms"

    medicine = models.ForeignKey(Medicine)
    medicineList = models.ManyToManyField(MedicineList)
    pharmaceutical_form_type =  models.ForeignKey(PharmaceuticalFormType)
    atc_code = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    

    def medicine_id(self):
        return unicode(self.medicine.id)

    def __unicode__(self):
        return unicode(self.pharmaceutical_form_type)

