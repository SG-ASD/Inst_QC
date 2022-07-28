from django.contrib import admin
from .models import Settings
from import_export.admin import ImportExportMixin

# Register your models here.
# admin.site.register(Settings)


# # @admin.register(Settings)
# class SettingsAdmin(ImportExportMixin, admin.ModelAdmin):
#     list_display = [
#         'Inspection_Path',
#         'Nonconformance_Path',
#     ]
#     list_display_links = [
#         'Inspection_Path',
#         'Nonconformance_Path',
#     ]

@admin.register(Settings)
class RevisionAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['Type',
                    'Path',
                    'Path_Describe',
                    ]
    list_display_links = ['Type']
    list_filter = ['Type']

    class Meta:
        db_table = 'Instrumentapp_revision'
        verbose_name = "문서개정 데이터"
        verbose_name_plural = "문서개정 데이터"