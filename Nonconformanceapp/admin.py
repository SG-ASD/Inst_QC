from django.contrib import admin
from .models import Nonconformance, Add_Nonconformance, Ref_Nonconformance
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin

# Register your models here.
admin.site.register(Nonconformance)
admin.site.register(Add_Nonconformance)


@admin.register(Ref_Nonconformance)
class Ref_NonconformanceAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = [
        'Category',
        'Type',
        'Part_Num',
        'Part_Name',
    ]
    list_display_links = [
        'Part_Num',
        'Part_Name',
    ]
    list_filter = [
        'Category',
        'Type',
        'Part_Num',
        'Part_Name',
    ]
    search_fields = [
        'Category',
        'Type',
        'Part_Num',
        'Part_Name',
    ]