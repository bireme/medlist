#! coding: utf-8
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

# tabular: tradução de medicine (inserido em MedicineAdmin)
class MedicineLocalAdmin(admin.TabularInline):
	model = MedicineLocal
	extra = 1

# tabular: tradução de forma farmaceutica (inserido em PharmaceuticalFormAdminTabular)
class PharmaceuticalFormTypeLocalAdminTabular(admin.TabularInline):
	model = PharmaceuticalFormTypeLocal
	extra = 1

class PharmaceuticalFormTypeAdmin(admin.ModelAdmin):
	model = PharmaceuticalFormType
	inlines = [PharmaceuticalFormTypeLocalAdminTabular, ]

class CompositionAdminTabular(admin.TabularInline):
	model = Composition
	extra = 1

class PharmaceuticalFormAdmin(admin.ModelAdmin):
	model = PharmaceuticalForm
	inlines = [CompositionAdminTabular, ]

class PharmaceuticalFormAdminTabular(admin.TabularInline):
	model = PharmaceuticalForm
	extra = 1

class MedicineAdmin(admin.ModelAdmin):
	model = Medicine
	inlines = [MedicineLocalAdmin, PharmaceuticalFormAdminTabular]

admin.site.register(Language)
admin.site.register(PharmaceuticalForm, PharmaceuticalFormAdmin)
admin.site.register(PharmaceuticalFormType, PharmaceuticalFormTypeAdmin)
admin.site.register(Medicine, MedicineAdmin)