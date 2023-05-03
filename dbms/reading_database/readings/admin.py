from django.contrib import admin
from .models import reading, table_reading
# Register your models here.

class ReadingAdmin(admin.ModelAdmin):
    list_display = ['time_of_recording', 'reading_value', 'reading_details']

class ReadingTableAdmin(admin.ModelAdmin):
    list_display = ['time_of_recording', 'reading_value', 'reading_details']


admin.site.register(reading, ReadingAdmin)
admin.site.register(table_reading, ReadingTableAdmin)
