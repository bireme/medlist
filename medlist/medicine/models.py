from django.db import models

class Medicine(models.Model):

	MedicineID = models.AutoField(primary_key=True)
	Abbreviation = models.CharField('Abreviation', max_length=50, null=True)

class Language(models.Model):

	class Meta:
		verbose_name = "Language"
		verbose_name_plural = "Languages"
	
	def __unicode__(self):
		return self.Name

	LangID = models.CharField(max_length=3, primary_key=True)
	Name = models.CharField('Name', max_length=30)

class Medicine_Local(models.Model):

	LangID = models.ForeignKey(Language,verbose_name='Language Identification')
	MedicineID = models.ForeignKey(Medicine,verbose_name='Medicine Identification')
	MedicineName = models.CharField('Medicine Name', max_length=250)

class MedicineRef(models.Model):

	MedicineRefID = models.AutoField(primary_key=True)
	MedicineID = models.ForeignKey(Medicine,verbose_name='Medicine Identification')
	Hyperlink = models.CharField('Hyperlink', max_length=500)
	MedicineRefDesc = models.TextField('Description')
	MedicineRefType = models.CharField('Type', max_length=30, blank=True, null=True)
	MedicineRefOrder = models.IntegerField('Order')
	
class MedicineAppStatus(models.Model):

	MedicineAppStatusID = models.AutoField(primary_key=True)
	MedicineAppStatusName = models.CharField('Name',max_length=10)

class MedicineAppType(models.Model):

	MedicineAppTypeID = models.AutoField(primary_key=True)

class MedicineAppType_Local(models.Model):

	MedicineAppTypeID = models.ForeignKey(MedicineAppType)
	LangID = models.ForeignKey(Language,verbose_name='Language Identification')
	MedicineAppTypeName = models.CharField('Name',max_length=50)

class MedicineApp(models.Model):

	MedicineAppID = models.AutoField(primary_key=True)
	MedicineID = models.ForeignKey(Medicine, verbose_name='Medicine')
	MedicineAppTypeID = models.ForeignKey(MedicineAppType, verbose_name='Medicine Aplication Type')
	EMLRef1 = models.CharField('EML Reference', max_length=10, blank=True, null=True)
	EMLSquareBox = models.IntegerField('EML Square Box', blank=True, null=True)
	ATC_code = models.CharField('ATC Code', max_length=10, blank=True, null=True)
	MedicineAppStatusID = models.ForeignKey(MedicineAppStatus, verbose_name="Medicine Aplication Status", blank=True, null=True)
	Sectionid = models.IntegerField('Section ID', blank=True, null=True)
	ApplyToChildrenOnly = models.BooleanField('Apply to Children Only?', blank=True)
	NotApplicableForChildren = models.BooleanField('Not Applicable For Children?', blank=True)







