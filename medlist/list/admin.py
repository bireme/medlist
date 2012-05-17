#! coding: utf-8
from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from models import *
from urllib2 import urlopen
from app_actions import create_list_archive
from django import forms
from medlist.history.models import *

class ListLocalAdmin(admin.TabularInline):
    model = ListLocal
    extra = 0

class SectionLocalAdmin(admin.TabularInline):
    model = SectionLocal
    extra = 0

class SectionPharmFormAdmin(admin.StackedInline):
	raw_id_fields = ("pharmaceutical_form",)
	model = SectionPharmForm
	extra = 0


class SectionAdmin(admin.ModelAdmin):

	inlines = [SectionLocalAdmin, SectionPharmFormAdmin, ]	
	list_display = ('id', 'title', 'get_list_abbreviation', 'get_hierarchy')
	list_filter = ('list__abbreviation', )
	search_fields = ('title', 'observation', 'id')   

	fields = ('title', 'list', 'parent', 'observation')    

class ListAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'abbreviation', 'type','get_link_list', 'published')
	list_filter = ('type', 'year')
	search_fields = ('abbreviation', 'name', 'id')
	actions = ['make_published', 'archive_list']
	inlines = [ListLocalAdmin, ]

	def get_link_list(self, obj):
		output = '<a href="/list/%s/?preview" target="_blank">Link</a>' % obj.id
		return unicode(output)
	get_link_list.allow_tags = True

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

	list_display = ("id", "__unicode__", 'section')
	list_filter = ("best_evidence", "only_for_children", "specialist_care_for_children",)
	search_fields = ("id", 'pharmaceutical_form__medicine__name', 'pharmaceutical_form__composition')
	raw_id_fields = ("section", "pharmaceutical_form")

	actions = ['index', ]

	# adding option to activate or not a register
	def index(modeladmin, request, queryset):
		for obj in queryset:
			obj.save()
	index.short_description = _("Indexes these pharmaceutical forms")

admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(SectionPharmForm, SectionPharmFormAdmin)
