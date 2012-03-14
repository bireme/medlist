#! coding: utf-8
from django.contrib import admin
from models import *
from django.utils.translation import ugettext_lazy as _

class PharmaceuticalFormAdmin(admin.StackedInline):
    model = PharmaceuticalForm
    extra = 0

class PharmaceuticalFormTypeLocalAdmin(admin.TabularInline):
    model = PharmaceuticalFormTypeLocal
    extra = 0

class MedicineLocalAdmin(admin.TabularInline):
    model = MedicineLocal
    extra = 0

class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    inlines = [MedicineLocalAdmin, PharmaceuticalFormAdmin]

    list_display = ('__unicode__', 'get_link_medicine', 'active')
    list_display_links = ('__unicode__',)
    search_fields = ('name', )
    list_filter = ('active', )

    actions = ['make_active']

    def get_link_medicine(self, obj):
        output = '<a href="/medicine/%s" target="_blank">Link</a>' % obj.id
        return unicode(output)
    get_link_medicine.allow_tags = True

    # removes delete option
    def has_delete_permission(self, request, obj=None):
        return False

    # adding option to activate or not a register
    def make_active(modeladmin, request, queryset):
        for obj in queryset:
            if obj.active:
                obj.active = False
            else:
                obj.active = True
            obj.save()
    make_active.short_description = _("Activate or deactivate selected medicines")

class PharmaceuticalFormTypeAdmin(admin.ModelAdmin):
    model = PharmaceuticalFormType
    inlines = [PharmaceuticalFormTypeLocalAdmin]

    list_display = ('__unicode__',)
    search_fields = ('name',)

class PharmaceuticalFormAdmin(admin.ModelAdmin):
    model = PharmaceuticalForm
    
    list_display = ('__unicode__', 'composition', 'medicine', 'atc_code', 'active')
    search_fields = ('pharmaceutical_form_type__name', 'atc_code', 'composition')
    list_filter = ('pharmaceutical_form_type__name', 'active')

    actions = ['make_active']

    # removes delete option
    def has_delete_permission(self, request, obj=None):
        return False

    # adding option to activate or not a register
    def make_active(modeladmin, request, queryset):
        for obj in queryset:
            if obj.active:
                obj.active = False
            else:
                obj.active = True
            obj.save()
    make_active.short_description = _("Activate or deactivate selected medicines")



admin.site.register(PharmaceuticalFormType, PharmaceuticalFormTypeAdmin)
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(PharmaceuticalForm, PharmaceuticalFormAdmin)
