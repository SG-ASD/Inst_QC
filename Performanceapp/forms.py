from django.forms import ModelForm

from Inspectionapp.models import Inspection


class Performance_first(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Perfomance_CoverSafety',
            'Perfomance_Barcode',
            'Perfomance_XYZpositioning',
            'Perfomance_HHS_SN',
            'Perfomance_HHS_temperature',
            'Perfomance_HHS_RPM',
            'Perfomance_Loading_TipCarrier',
            'Perfomance_Loading_TubeCarrier',
            'Perfomance_Loading_mtpCarrier',
            'Perfomance_Loading_4mfxCarrier',
        ]

class Performance_second(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Perfomance_VFV_Accuracy300ul1',
            'Perfomance_VFV_Accuracy300ul2',
            'Perfomance_VFV_Accuracy300ul3',
            'Perfomance_VFV_Accuracy300ul4',
            'Perfomance_VFV_Accuracy300ul5',
            'Perfomance_VFV_Accuracy300ul6',
            'Perfomance_VFV_Accuracy300ul7',
            'Perfomance_VFV_Accuracy300ul8',

            'Perfomance_VFV_Precision300ul1',
            'Perfomance_VFV_Precision300ul2',
            'Perfomance_VFV_Precision300ul3',
            'Perfomance_VFV_Precision300ul4',
            'Perfomance_VFV_Precision300ul5',
            'Perfomance_VFV_Precision300ul6',
            'Perfomance_VFV_Precision300ul7',
            'Perfomance_VFV_Precision300ul8',

            'Perfomance_VFV_Accuracy1000ul1',
            'Perfomance_VFV_Accuracy1000ul2',
            'Perfomance_VFV_Accuracy1000ul3',
            'Perfomance_VFV_Accuracy1000ul4',
            'Perfomance_VFV_Accuracy1000ul5',
            'Perfomance_VFV_Accuracy1000ul6',
            'Perfomance_VFV_Accuracy1000ul7',
            'Perfomance_VFV_Accuracy1000ul8',

            'Perfomance_VFV_Precision1000ul1',
            'Perfomance_VFV_Precision1000ul2',
            'Perfomance_VFV_Precision1000ul3',
            'Perfomance_VFV_Precision1000ul4',
            'Perfomance_VFV_Precision1000ul5',
            'Perfomance_VFV_Precision1000ul6',
            'Perfomance_VFV_Precision1000ul7',
            'Perfomance_VFV_Precision1000ul8',
        ]

