#! coding: utf-8

from django.db import models
from datetime import datetime
from medlist import settings

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
        return unicode(self.name)    

class Country(models.Model):

    class Meta:
        verbose_name = "Country"
        verbose_name_plural = "Countries"

    abbreviation = models.CharField(max_length=20)
    name = models.CharField(max_length=255)    
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    
    def __unicode__(self): 
        return unicode(self.name)    


class Medicine(models.Model):

    name = models.CharField(max_length=255)
    obs = models.TextField()
    
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

class EvidenceSummary(models.Model):

    class Meta:
        verbose_name = "Evidences Summary"
        verbose_name_plural = "Evidence Summaries"

    title = models.CharField(max_length=255)
    abstract = models.TextField()
    pharmaceutical_form = models.ForeignKey('PharmaceuticalForm')
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)

    def __unicode__(self):
        return unicode(self.title)

class EvidenceSummaryLocal(models.Model):

    class Meta:
        verbose_name = "Evidences Summary Translation"
        verbose_name_plural = "Evidence Summary Translations"

    evidence = models.ForeignKey(EvidenceSummary)
    language = models.CharField(max_length=10, choices=LANGUAGES_CHOICES)
    title = models.CharField(max_length=255)
    abstract = models.TextField()

    date_creation = models.DateTimeField(default=datetime.now, editable=False)

    def __unicode__(self):
        return unicode(self.title)

class EvidenceSummaryUpload(models.Model):

    class Meta:
        verbose_name = "Evidences Summary File"
        verbose_name_plural = "Evidence Summary Files"

    evidence = models.ForeignKey(EvidenceSummary)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to=settings.MEDIA_ROOT)

    date_creation = models.DateTimeField(default=datetime.now, editable=False)

    def __unicode__(self):
        return unicode(self.title)

    def get_relative_url(self):
        return self.file.url.replace(settings.PROJECT_ROOT_PATH, u'')

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
    medicineList = models.ManyToManyField(MedicineList, blank=True)
    pharmaceutical_form_type =  models.ForeignKey(PharmaceuticalFormType)
    atc_code = models.CharField(max_length=255)
    composition = models.CharField(max_length=255)
    countries = models.ManyToManyField(Country, blank=True)
    obs = models.TextField()
    
    date_creation = models.DateTimeField(default=datetime.now, editable=False)
    

    def medicine_id(self):
        return unicode(self.medicine.id)

    def __unicode__(self):
        output = "%s - %s (%s)" % (self.medicine, self.pharmaceutical_form_type, self.atc_code)
        return unicode(output)

