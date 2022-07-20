from django.contrib import admin
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.html import format_html
from import_export import fields, resources
from import_export.admin import ExportActionModelAdmin, ImportExportMixin, ImportMixin
from .models import Calibration


# Register your models here.
@admin.register(Calibration)
class CalibrationAdmin(ImportExportMixin, admin.ModelAdmin):
    list_display = ['is_Hide',
                    'styled_status',
                    'Instrument',
                    'Mgt_Num',
                    'Equipment_Name',
                    'CAL_Type',
                    'CAL_Cycle',
                    'CAL_Date',
                    'Expiration_Date',
                    'CAL_Plan_Date',
                    'Serial_Num',
                    'ERP_Num',
                    'Head',
                    'Deputy_Head',
                    'Store_Location',
                    # 'price_format',
                    'Ramarks',
                    ]
    list_display_links = ['Mgt_Num']
    list_filter = ['Status', 'Instrument','Mgt_Num','Equipment_Name']
    search_fields = ['Mgt_Num']

    def styled_status(self, obj):
        # obj : 레코드
        # f string : python 최신 문법
        # 다양한 문자열 연결
        # 1. + 연결 : '<b>'+obj.status + '</b>'
        # 2. % format : '<b>%s</b>'%(obj.status)
        # 3. format 함수 : '<b>{}</b>'.format(obj.status)
        # 4. f-string : f'<b>{obj.status}</b>'
        if obj.Status == '가능':
            return format_html(f'<span style="color:green; font-weight:bold">{obj.Status}</span>')
        if obj.Status == '교정예정':
            return format_html(f'<span style="color:blue; font-weight:bold">{obj.Status}</span>')
        if obj.Status == '교정중':
            return format_html(f'<span style="color:red; font-weight:bold">{obj.Status}</span>')
        if obj.Status == '불가(고장)' or obj.Status == '불가(기타)':
            return format_html(f'<span style="color:grey; font-weight:bold">{obj.Status}</span>')
        if obj.Status == '불가(미등록)' or obj.Status == '불가(미입고)':
            return format_html(f'<span style="color:orange; font-weight:bold">{obj.Status}</span>')
        return format_html(f'<span">{obj.Status}</span>')
    styled_status.short_description = "상태표시 알림"

    def price_format(self, obj):
        Price = intcomma(obj.Price)
        return f'{Price} 원'

    price_format.short_description = '가격'





