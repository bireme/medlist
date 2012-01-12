from django.contrib import admin
from models import *

class MedicineAppType_LocalAdmin(admin.ModelAdmin):
	model = MedicineAppType_Local
	list_display = ('MedicineAppTypeName', 'MedicineAppTypeID')

class MedicineAppAdmin(admin.ModelAdmin):
	model = MedicineApp
	list_display = ('MedicineAppID', 'MedicineID', 'EMLRef1', 'EMLSquareBox', 'ATC_code', 'MedicineAppStatusID', 'Sectionid', 'ApplyToChildrenOnly', 'NotApplicableForChildren')

admin.site.register(Medicine)
admin.site.register(Language)
admin.site.register(Medicine_Local)
admin.site.register(MedicineRef)
admin.site.register(MedicineAppStatus)
admin.site.register(MedicineAppType)
admin.site.register(MedicineAppType_Local, MedicineAppType_LocalAdmin)
admin.site.register(MedicineApp, MedicineAppAdmin)