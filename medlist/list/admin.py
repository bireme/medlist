#! coding: utf-8

from django.utils.translation import ugettext_lazy as _
from django.contrib import admin
from models import *
from urllib2 import urlopen
from app_actions import create_list_archive
from medlist.history.models import *
import json

class SectionPharmFormAdmin(admin.StackedInline):
	model = SectionPharmForm
	extra = 0

class SectionAdmin(admin.ModelAdmin):

	inlines = (SectionPharmFormAdmin, )
	list_display = ('title', 'get_list_abbreviation', 'get_hierarchy')
	list_filter = ('list__abbreviation', )
	search_fields = ('section', 'list')

class ListAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'abbreviation', 'type','get_link_list', 'published')
	list_filter = ('type', 'year')
	search_fields = ('abbreviation', 'name', 'id')
	actions = ['make_published', 'archive_list']

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


admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
