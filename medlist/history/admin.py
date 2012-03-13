from django.contrib import admin
from models import *

class HistoryAdmin(admin.ModelAdmin):
	list_display = ('name', 'type', 'year', 'created')
	search_fields = ('name', 'subtype', 'type', 'year')
	list_filter = ('type', 'subtype', 'year')

	def has_delete_permission(self, request, obj=None):
		return False

admin.site.register(History, HistoryAdmin)