from django.contrib import admin
from models import *

"""class MedicineLocalAdmin(admin.TabularInline):
	model = MedicineLocal
	extra = 1

class MedicineDrugsAdmin(admin.TabularInline):
	model = MedicineDrugs
	extra = 1

class DrugLocalAdmin(admin.TabularInline):
	model = DrugLocal
	extra = 1

class MedicineAdmin(admin.ModelAdmin):
	model = Medicine
	inlines = [MedicineLocalAdmin, MedicineDrugsAdmin]

class DrugAdmin(admin.ModelAdmin):
	model = Drug
	inlines = [DrugLocalAdmin]

class LanguageAdmin(admin.ModelAdmin):
	model = Language
	list_display = ('abbreviation', 'name', 'creation_date')

admin.site.register(Language, LanguageAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Drug, DrugAdmin)

#admin.site.register(MedicineLocal)
admin.site.register(DosageForm)
admin.site.register(DosageFormLocal)
admin.site.register(MedicinePharmaceuticalForm)
admin.site.register(MedicineApplication)"""

class MedicineLocalAdmin(admin.TabularInline):
	model = MedicineLocal
	extra = 1

class CompositionAdmin(admin.TabularInline):
	model = Composition
	extra = 1

class PharmaceuticalFormAdmin(admin.TabularInline):
	model = PharmaceuticalForm
	extra = 1
	inlines = [CompositionAdmin, ]



class MedicineAdmin(admin.ModelAdmin):
	model = Medicine
	inlines = [MedicineLocalAdmin, PharmaceuticalFormAdmin]

admin.site.register(Language)
admin.site.register(PharmaceuticalFormType)
admin.site.register(Medicine, MedicineAdmin)