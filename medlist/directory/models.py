#! coding: utf-8
from django.db import models
from datetime import datetime

LANGUAGES_CHOICES = (
    ('pt-br', 'Português Brasil'),
    ('es', 'Espanhol'),
)

class MedicineList(models.Model):
    abbreviation = models.CharField(max_length=20)
    name = models.CharField(max_length=255)    
    
    def __unicode__(self): 
        return unicode(self.abbreviation)    


class Medicine(models.Model):
    name = models.CharField(max_length=255)
    def __unicode__(self):
        return unicode(self.name)


# Tabela com itens traduzidos do Model Medicine
class MedicineLocal(models.Model):
    medicine = models.ForeignKey(Medicine)
    language = models.CharField(max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(max_length=255)
    
    class Meta:
        verbose_name = "Medicine Translation"
        verbose_name_plural = "Medicine Translations"


#vocabulario controlado
class PharmaceuticalFormType(models.Model):    
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return unicode(self.name)

# local do PharmaceuticalFormType
class PharmaceuticalFormTypeLocal(models.Model):

    pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType)
    language = models.CharField(max_length=10, choices=LANGUAGES_CHOICES)
    name = models.CharField(max_length=255)


class PharmaceuticalForm(models.Model):
    medicine = models.ForeignKey(Medicine)
    medicineList = models.ManyToManyField(MedicineList)
    pharmaceutical_form_type =  models.ForeignKey(PharmaceuticalFormType)
    atc_code = models.CharField(max_length=255)
    coposition = models.CharField(max_length=255)

    def medicine_id(self):
        return unicode(self.medicine.id)

    def __unicode__(self):
        return unicode(self.pharmaceutical_form_type)

