from django.db import models
from medlist.directory.models import PharmaceuticalForm

class List(models.Model):

	class Meta:
		verbose_name = u"list"
		verbose_name_plural = u"lists"

	name = models.CharField(max_length=255)
	abbreviation = models.CharField(max_length=50)
	year = models.IntegerField()
	is_special = models.BooleanField()
	is_country = models.BooleanField()

	def __unicode__(self):
		return unicode(self.name)

class Section(models.Model):

	class Meta:
		verbose_name = u"section"
		verbose_name_plural = u"sections"

	title = models.CharField(max_length=255)
	parent = models.ForeignKey('Section', blank=True, null=True)
	list = models.ForeignKey(List)
	
	def __unicode__(self):
		return unicode(self.title)	

	def get_list_abbreviation(self):
		return unicode(self.list.abbreviation)		

class SectionPharmForm(models.Model):
	
	section = models.ForeignKey(Section)
	pharmaceutical_form = models.ForeignKey(PharmaceuticalForm)
