from django.contrib import admin
from .models import Settings
from import_export.admin import ImportExportMixin

# Register your models here.
admin.site.register(Settings)


# @admin.register(Settings)
class SettingsAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'Inspection_Path',
        'Nonconformance_Path',
    ]
    list_display_links = [
        'Inspection_Path',
        'Nonconformance_Path',
    ]
