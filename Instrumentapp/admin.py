from django.contrib import admin
from .models import Instrument, Revision
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
admin.site.register(Instrument)

@admin.register(Revision)
class RevisionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Instrument',
                    'Report_Category',
                    'Rev_Num',
                    'Rev',
                    'Start_Dt',
                    'End_Dt',
                    ]
    list_display_links = ['Instrument']
    list_filter = ['Instrument', 'Report_Category', 'Start_Dt']
    search_fields = ['Rev_Num']

    class Meta:
        db_table = 'Instrumentapp_revision'
        verbose_name = "문서개정 데이터"
        verbose_name_plural = "문서개정 데이터"
