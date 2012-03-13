#! coding: utf-8

from django.contrib import admin
from models import *
from urllib2 import urlopen
from medlist.history.models import *
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
	actions = ['archivate_list']

	def get_link_list(self, obj):
		output = '<a href="/list/%s" target="_blank">Link</a>' % obj.id
		return unicode(output)
	get_link_list.allow_tags = True

	def archivate_list(self, request, queryset):

		for obj in queryset:
				
			history = History()

			history.name = obj.name
			history.year = obj.year
			history.type = obj.type
			history.subtype = obj.subtype
			history.content = json.dumps('aqui vem o conteudo serializado')
			
			history.save()


admin.site.register(Section, SectionAdmin)
admin.site.register(List, ListAdmin)
