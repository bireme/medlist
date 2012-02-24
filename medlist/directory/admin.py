#! coding: utf-8
from django.contrib import admin
from models import *


# tabular: tradução de forma farmaceutica (inserido em PharmaceuticalFormAdminTabular)
class PharmaceuticalFormAdmin(admin.TabularInline):
    model = PharmaceuticalForm
    extra = 1

class PharmaceuticalFormTypeLocalAdmin(admin.TabularInline):
    model = PharmaceuticalFormTypeLocal
    extra = 1

class MedicineLocalAdmin(admin.TabularInline):
    model = MedicineLocal
    extra = 1

class MedicineListAdmin(admin.TabularInline):
    model = MedicineList
    extra = 1

class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    inlines = [MedicineLocalAdmin, PharmaceuticalFormAdmin]


class PharmaceuticalFormTypeAdmin(admin.ModelAdmin):
    model = PharmaceuticalFormType
    inlines = [PharmaceuticalFormTypeLocalAdmin]

admin.site.register(PharmaceuticalFormType, PharmaceuticalFormTypeAdmin)
admin.site.register(MedicineList)
admin.site.register(Medicine, MedicineAdmin)
