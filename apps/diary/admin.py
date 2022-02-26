from django.contrib import admin
from .models import Entry, FinalRecordID

class DataEntry(admin.ModelAdmin):
    fields = ['entry_id', 'user', 'entry']

class DataFinalRecordID(admin.ModelAdmin):
    fields = ['final_id', 'user']

admin.site.register(Entry, DataEntry)
admin.site.register(FinalRecordID, DataFinalRecordID)