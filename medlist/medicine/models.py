#! coding: utf-8
from django.db import models
from datetime import datetime

# Linguagens dos dados disponíveis no sistema
class Language(models.Model):
	
	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Languages'

	def __unicode__(self):
		return str(self.abbreviation)

	abbreviation = models.CharField(max_length=2)
	name = models.CharField(max_length=255)
	creation_date = models.DateTimeField(editable=False, default=datetime.now())

class Medicine(models.Model):

	id = models.AutoField(primary_key=True)

	def __unicode__(self):
		translations = MedicineLocal.objects.filter(medicine=self.id)
		if len(translations) > 0:
			return translations[0].name
		else:
			return str('No Labels')

# Tabela com itens traduzidos do Model Medicine
class MedicineLocal(models.Model):

	class Meta:
		verbose_name = "Medicine Translation"
		verbose_name_plural = "Medicine Translations"

	medicine = models.ForeignKey(Medicine)
	language = models.ForeignKey(Language)
	name = models.CharField(max_length=255)

class Drug(models.Model):

	id = models.AutoField(primary_key=True)

# Tabela com itens traduzidos do Model Drug
class DrugLocal(models.Model):
	
	drug = models.ForeignKey(Drug)
	language = models.ForeignKey(Language)
	name = models.CharField(max_length=255)

#vocabulario controlado
class PharmaceuticalFormType(models.Model):

	id = models.AutoField(primary_key=True)

	def __unicode__(self):
		translations = PharmaceuticalFormTypeLocal.objects.filter(pharmaceutical_form_type=self.id)
		if len(translations) > 0:
			return translations[0].name
		else:
			return str('No Labels')

# local do PharmaceuticalFormType
class PharmaceuticalFormTypeLocal(models.Model):

	pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType)
	language = models.ForeignKey(Language)
	name = models.CharField(max_length=255)

class PharmaceuticalForm(models.Model):

	medicine = models.ForeignKey(Medicine)
	pharmaceutical_form_type = models.ForeignKey(PharmaceuticalFormType)
	only_for_children = models.BooleanField()
	only_for_adult = models.BooleanField()

class PharmaceuticalFormLocal(models.Model):
	
	language = models.ForeignKey(Language)
	pharmaceutical_form = models.ForeignKey(PharmaceuticalForm)	
	label = models.CharField(max_length=255)

class MedicineApplication(models.Model):

	id = models.AutoField(primary_key=True)
	medicine = models

# traduzir atraves da tradução do django
class NoteType(models.Model):

	name = models.CharField(max_length=255)

class Note(models.Model):

	type = models.ForeignKey(NoteType)
	pharmaceutical_form = models.ForeignKey(PharmaceuticalForm, null=True, blank=True)
	medicine_application = models.ForeignKey(MedicineApplication, null=True, blank=True)

class NoteLocal(models.Model):

	language = models.ForeignKey(Language)
	note = models.ForeignKey(Note)
	description = models.CharField(max_length=255)

class Composition(models.Model):

	pharmaceutical_form = models.ForeignKey(PharmaceuticalForm)
	drug = models.ForeignKey(Drug)
	concentration = models.CharField(max_length=255)

# Listas

class List(models.Model):

	country_list = models.BooleanField() # flag se é lista de país, ou outro tipo de lista
	especial_list = models.BooleanField() # se é algum tipo High Cost, por exemplo (???)

# Traduções da lista
class ListLocal(models.Model):

	language = models.ForeignKey(Language)
	list = models.ForeignKey(List)
	name = models.CharField(max_length=255)

# sessão de uma lista
class Section(models.Model):

	parentID = models.ForeignKey('self', null=True) # FK para marcar os subniveis de seção
	list = models.ForeignKey(List)
	complementary = models.BooleanField()


class SectionLocal(models.Model):

	language = models.ForeignKey(Language)
	section = models.ForeignKey(Section)
	name = models.CharField(max_length=255)





# OBS:
# - O que for tradução de labels do sistema, retirar as traduções da modelagem.
# - Estudar qual a melhor relação de PharmaceuticalForm: se relacionar com MedicineApplication ou Medicine