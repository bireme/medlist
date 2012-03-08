#! coding: utf-8
from django.contrib import admin
from models import *

class PharmaceuticalFormAdmin(admin.StackedInline):
    model = PharmaceuticalForm
    extra = 1

class PharmaceuticalFormTypeLocalAdmin(admin.TabularInline):
    model = PharmaceuticalFormTypeLocal
    extra = 1

class MedicineLocalAdmin(admin.TabularInline):
    model = MedicineLocal
    extra = 1

class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    inlines = [MedicineLocalAdmin, PharmaceuticalFormAdmin]

    list_display = ('__unicode__', 'date_creation',)
    list_filter = ('date_creation', )
    list_display_links = ('__unicode__',)
    search_fields = ('name', )


class PharmaceuticalFormTypeAdmin(admin.ModelAdmin):
    model = PharmaceuticalFormType
    inlines = [PharmaceuticalFormTypeLocalAdmin]

    list_display = ('__unicode__',)
    search_fields = ('name',)

class PharmaceuticalFormAdmin(admin.ModelAdmin):
    model = PharmaceuticalForm
    
    list_display = ('__unicode__', 'composition', 'medicine', 'atc_code')
    search_fields = ('pharmaceutical_form_type__name', 'atc_code', 'composition')
    list_filter = ('pharmaceutical_form_type__name',)


admin.site.register(PharmaceuticalFormType, PharmaceuticalFormTypeAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PharmaceuticalForm, PharmaceuticalFormAdmin)
