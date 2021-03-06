#! coding: utf-8
from django import forms
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from django.shortcuts import redirect

from list.app_actions import create_list_archive
from list.index import update_index
from history.models import *

from list.models import *

class ListLocalAdmin(admin.TabularInline):
    model = ListLocal
    extra = 0

class SectionLocalAdmin(admin.StackedInline):
    model = SectionLocal
    extra = 0

class SectionPharmFormAdmin(admin.StackedInline):
    autocomplete_fields = ('pharmaceutical_form', )
    model = SectionPharmForm
    extra = 0


class SectionAdmin(admin.ModelAdmin):
    inlines = [SectionLocalAdmin, SectionPharmFormAdmin, ]
    list_display = ('title', 'get_list_abbreviation', 'get_hierarchy')
    list_filter = ('list__abbreviation', )
    search_fields = ('title', 'observation', 'id')

    fields = ('title', 'list', 'parent', 'observation')


    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'list':
            list_id = request.GET.get('list_id')
            kwargs['initial'] = list_id
            return db_field.formfield(**kwargs)
        elif db_field.name == 'parent':
            parent_id = request.GET.get('parent_id')
            kwargs['initial'] = parent_id
            return db_field.formfield(**kwargs)

        return super(SectionAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def response_add(self, request, obj):
        return redirect('/close_window')

    def response_change(self, request, obj):
        return redirect('/close_window')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/close_window')


class ListAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbreviation', 'type','get_link_list', 'published')
    list_filter = ('type', 'year')
    search_fields = ('abbreviation', 'name', 'id')
    actions = ['make_published', 'archive_list']
    inlines = [ListLocalAdmin, ]

    def get_link_list(self, obj):
        output = '<a href="/list/%s/?preview" target="_blank">Link</a>' % obj.id
        return mark_safe(output)

    # action that makes published
    def make_published(modeladmin, request, queryset):
        for obj in queryset:
            if not obj.published:
                obj.published = True
            else:
                obj.published = False
                obj.save()
    make_published.short_description = _("Published or unpublished selected lists")

    # action that makes published
    def archive_list(modeladmin, request, queryset):
        for obj in queryset:
            create_list_archive(obj)
            modeladmin.message_user(request, _("Created of list archive copy successfully"))

    archive_list.short_description = _("Create a archive copy of selected lists")

class SectionPharmFormAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'section')
    list_filter = ('best_evidence', 'only_for_children', 'specialist_care_for_children',)
    search_fields = ('id', 'pharmaceutical_form__medicine__name', 'pharmaceutical_form__composition')
    #raw_id_fields = ('section', 'pharmaceutical_form')
    autocomplete_fields = ('section', 'pharmaceutical_form')

    actions = ['index', ]

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        print(db_field.name)
        if db_field.name == 'section':
            section_id = request.GET.get('section_id')
            kwargs['initial'] = section_id
            return db_field.formfield(**kwargs)

        return super(SectionPharmFormAdmin, self).formfield_for_foreignkey(db_field, request, **kwargs)

    def response_add(self, request, obj):
        return redirect('/close_window')

    def response_change(self, request, obj):
        return redirect('/close_window')

    def response_delete(self, request, obj_display, obj_id):
        return redirect('/close_window')


    # adding option to activate or not a register
    def index(modeladmin, request, queryset):
        for obj in queryset:
            obj.save()

    index.short_description = _("Indexes these pharmaceutical forms")

admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(SectionPharmForm, SectionPharmFormAdmin)
