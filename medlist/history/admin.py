from django.contrib import admin
from models import *


class HistoryLocalAdmin(admin.TabularInline):    
    readonly_fields = ('language', 'name', 'obs', 'xml', 'content',)
    model = HistoryLocal
    extra = 0

class HistoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    readonly_fields = ('name', 'abbreviation', 'obs', 'edition', 'type', 'subtype', 'year', 'created', 'xml', 'content')
    search_fields = ('name', 'subtype', 'type', 'year')
    list_filter = ('type', 'subtype', 'year')
    inlines = [HistoryLocalAdmin, ]

    #def has_delete_permission(self, request, obj=None):
    #   return False

admin.site.register(History, HistoryAdmin)