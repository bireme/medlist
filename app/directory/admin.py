#! coding: utf-8
from django.contrib import admin
from django.contrib import messages
from models import *
from app_actions import solr_index
from django.utils.translation import ugettext_lazy as _
from evidence.models import *

class PharmaceuticalFormAdmin(admin.StackedInline):
    model = PharmaceuticalForm
    extra = 0

class MedicineEvidenceSummaryInline(admin.StackedInline):
    model = MedicineEvidenceSummary
    raw_id_fields = ("evidence", )
    extra = 0

class PharmaceuticalFormTypeLocalAdmin(admin.TabularInline):
    model = PharmaceuticalFormTypeLocal
    extra = 0

class MedicineLocalAdmin(admin.TabularInline):
    model = MedicineLocal
    extra = 0

class MedicineAdmin(admin.ModelAdmin):
    model = Medicine
    inlines = [MedicineLocalAdmin, PharmaceuticalFormAdmin, MedicineEvidenceSummaryInline]

    list_display = ('__unicode__', 'get_link_medicine', 'active')
    list_display_links = ('__unicode__',)
    search_fields = ('name', )
    list_filter = ('active', )

    actions = ['make_active', 'index']

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

    # adding option to index a medicine on Solr index
    def index(modeladmin, request, queryset):
        index_sucess = True
        for obj in queryset:
            index_sucess = solr_index(obj)

        if not index_sucess:
            messages.error(request, _("Unable to index medicines"))
        else:
            modeladmin.message_user(request, _("Selected medicines were indexed"))

    index.short_description = _("Index selected medicines")
    
    def save_formset(self, request, form, formset, change):        
        # save of related objects (formsets) are call after save_model 
        # so if one or more of related models are changed is necessary update Solr index again
        medicine_id = None
        instances = formset.save(commit=False)
        for instance in instances:
            medicine_id = instance.medicine.id
            instance.save()
        formset.save_m2m()
        
        # re-index on Solr the medicine object
        if medicine_id:
            medicine_obj = Medicine.objects.get(pk=medicine_id)
            solr_index(medicine_obj)
        

    def save_model(self, request, obj, form, change):
        obj.save()       
        
        index_sucess = solr_index(obj)
        if not index_sucess:
            messages.warning(request, _("Search index update fail."))


    def get_actions(self, request):
        actions = super(MedicineAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions        

class PharmaceuticalFormTypeAdmin(admin.ModelAdmin):
    model = PharmaceuticalFormType
    inlines = [PharmaceuticalFormTypeLocalAdmin]

    list_display = ('__unicode__',)
    search_fields = ('name',)

class PharmaceuticalFormAdmin(admin.ModelAdmin):
    model = PharmaceuticalForm
    
    list_display = ('medicine', 'composition',  'pharmaceutical_form_type', 'atc_code', 'active')
    search_fields = ('pharmaceutical_form_type__name', 'atc_code', 'composition', 'medicine__name')
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
