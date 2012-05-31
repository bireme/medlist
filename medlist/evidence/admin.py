from django.contrib import admin
from models import *

class EvidenceSummaryLocalInline(admin.StackedInline):
    model = EvidenceSummaryLocal
    extra = 0

class EvidenceSummaryAdmin(admin.ModelAdmin):

    inlines = (EvidenceSummaryLocalInline, )
    list_display = ('__unicode__', 'created', 'updated')
    search_fields = ('title', 'question', 'context', 'file', 'id')
    raw_id_fields = ('medicine',)

admin.site.register(EvidenceSummary, EvidenceSummaryAdmin)