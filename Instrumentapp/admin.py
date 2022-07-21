from django.contrib import admin
from .models import Instrument, Revision, Version
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
# Register your models here.
admin.site.register(Instrument)

@admin.register(Revision)
class RevisionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Instrument',
                    'Report_Category',
                    'Management_Num',
                    'Rev',
                    'Start_Dt',
                    'End_Dt',
                    'Etc'
                    ]
    list_display_links = ['Instrument']
    list_filter = ['Instrument', 'Report_Category', 'Start_Dt']
    search_fields = ['Management_Num']

    class Meta:
        db_table = 'Instrumentapp_revision'
        verbose_name = "문서개정 데이터"
        verbose_name_plural = "문서개정 데이터"

@admin.register(Version)
class VersionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Instrument',
                    'Inst_Label_Kor',
                    'Box_Label_Kor',
                    'Inst_Label_Eng',
                    'Box_Label_Eng',
                    'Etc',
                    ]
    list_display_links = ['Instrument']
    list_filter = ['Instrument']
    search_fields = ['Instrument']

    class Meta:
        db_table = 'Instrumentapp_revision'
        verbose_name = "문서개정 데이터"
        verbose_name_plural = "문서개정 데이터"