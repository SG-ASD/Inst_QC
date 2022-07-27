from django.contrib import admin
from .models import Instrument, Revision, Version
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
admin.site.register(Instrument)

@admin.register(Revision)
class RevisionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Management_Num',
                    'Revision',
                    'Instrument_Name',
                    'Type',
                    'Start_Dt',
                    'Expiry_Dt',
                    ]
    list_display_links = ['Management_Num']
    list_filter = ['Type', 'Instrument_Name', 'Start_Dt']
    search_fields = ['Type']

    class Meta:
        db_table = 'Instrumentapp_revision'
        verbose_name = "문서개정 데이터"
        verbose_name_plural = "문서개정 데이터"

@admin.register(Version)
class VersionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
                    'Type',
                    'Instrument_Name',
                    'SW_Name',
                    'SW_Ver',
                    'Start_Dt',
                    'Expiry_Dt',
                    'Remarks',
                    ]
    list_display_links = ['Instrument_Name']
    list_filter = ['Instrument_Name']
    search_fields = ['Instrument_Name']

    class Meta:
        db_table = 'Instrumentapp_version'
        verbose_name = "장비버전 데이터"
        verbose_name_plural = "장비버전 데이터"