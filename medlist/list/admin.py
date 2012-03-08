#! coding: utf-8

from django.contrib import admin
from models import *

def get_child(obj, list={}):
	if obj.parent:
		list[obj.id] = get_child()
	else:
		return list

class SectionPharmFormAdmin(admin.StackedInline):
	model = SectionPharmForm
	extra = 0

class SectionAdmin(admin.ModelAdmin):

	inlines = (SectionPharmFormAdmin, )
	list_display = ('__unicode__', 'get_list_abbreviation', 'get_number_section')

	def get_number_section(self, obj):
		
		sections = {}
		count = 1

		obj_sections = Section.objects.filter(list=obj.list)
		obj_sections = obj_sections.filter(parent=None)
		for section in obj_sections:
			
			tmp = {'number': count}
			tmp['children'] = {}
			count2 = 1

			for child in Section.objects.filter(parent=section.id):
					
				number = "%s.%s" % (count, count2)
				tmp2 = {'number': number}
				tmp['children'][child.id] = tmp2
				count2 += 1

				if child.id == obj.id:
					return number

			count += 1
			sections[section.id] = tmp

			if section.id == obj.id:
					return count

		return unicode()

admin.site.register(Section, SectionAdmin)
admin.site.register(List)