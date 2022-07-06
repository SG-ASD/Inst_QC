from django.contrib import admin

from .models import Calibration

# Register your models here.
@admin.register(Calibration)
class CalibrationAdmin(admin.ModelAdmin):
    list_display = ['Managemant_Num', 'Calibration_Serial','Instrument','Description','CalibrationDt', 'ValidationDt', 'State', 'is_Hide']
    list_display_links = ['Managemant_Num']
    list_filter = ['CalibrationDt', 'ValidationDt','Instrument']
    search_fields = ['Managemant_Num']



