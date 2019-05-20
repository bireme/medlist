from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from evidence.index import index_evidence
from evidence.models import *

class EvidenceSummaryLocalInline(admin.StackedInline):
    model = EvidenceSummaryLocal
    extra = 0

class EvidenceSummaryAdmin(admin.ModelAdmin):

    inlines = (EvidenceSummaryLocalInline, )
    list_display = ('title', 'created', 'updated')
    search_fields = ('title', 'question', 'context', 'file', 'id')

    actions = ['index']


    # adding option to index a medicine on Solr index
    def index(modeladmin, request, queryset):
        index_sucess = True
        for obj in queryset:
            index_sucess = index_evidence(obj)

        if not index_sucess:
            messages.error(request, _("Unable to index Evidence Summary"))
        else:
            modeladmin.message_user(request, _("Selected Evidences Summaries were indexed"))

    index.short_description = _("Index selected Evidences Summaries")


admin.site.register(EvidenceSummary, EvidenceSummaryAdmin)
