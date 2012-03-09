from django.db import models
from medlist.directory.models import PharmaceuticalForm
from mptt.models import MPTTModel, TreeForeignKey

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

class Section(MPTTModel):

	class Meta:
		verbose_name = u"section"
		verbose_name_plural = u"sections"

	class MPTTMeta:
		order_insertion_by = ['title']

	title = models.CharField(max_length=255)
	parent = TreeForeignKey('Section', blank=True, null=True, related_name='children')
	list = models.ForeignKey(List)
	hierarchy = models.CharField(max_length=10, blank=True, null=True)
	complementary_list = models.BooleanField()
	
	def __unicode__(self):
		output = "%s - %s" % (self.list.abbreviation, self.title)
		return unicode(output)	

	def get_parent_title(self):
		if self.parent:
			return unicode(self.parent.title)

	def get_list_abbreviation(self):
		return unicode(self.list.abbreviation)	


class SectionPharmForm(models.Model):
	
	section = models.ForeignKey(Section)
	pharmaceutical_form = models.ForeignKey(PharmaceuticalForm)
	only_for_children = models.BooleanField()
	specialist_care_for_children = models.BooleanField()
	observation = models.TextField(blank=True, null=True)
