#! coding: utf-8

from django.contrib import admin
from models import *
from urllib2 import urlopen
import json

class SectionPharmFormAdmin(admin.StackedInline):
	model = SectionPharmForm
	extra = 0

class SectionAdmin(admin.ModelAdmin):

	inlines = (SectionPharmFormAdmin, )
	list_display = ('title', 'get_list_abbreviation', 'get_parent_title')
	list_filter = ('list__abbreviation', )
	search_fields = ('section', 'list')

class ListAdmin(admin.ModelAdmin):

	list_display = ('__unicode__', 'abbreviation', 'type', 'get_link_list')
	list_filter = ('type', 'year')
	search_fields = ('abbreviation', 'name', 'id')

	def get_link_list(self, obj):
		output = '<a href="/list/%s" target="_blank">Link</a>' % obj.id
		return unicode(output)
	get_link_list.allow_tags = True


admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
