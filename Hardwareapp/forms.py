from django.forms import ModelForm

from Inspectionapp.models import Inspection


class HardwareUpdateForm_first(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'HardWare_CalibrationTool',
            'HardWare_BarcodeCarrier',
            'HardWare_XArm_left',
            'HardWare_XArm_right',
            'HardWare_XArm_Diff',
            'HardWare_Xdev1',
            'HardWare_Xdev2',
            'HardWare_Xdev3',
            'HardWare_Xdev4',
            'HardWare_Xdev5',
            'HardWare_Xdev6',
            'HardWare_Xdev7',
            'HardWare_Xdev8',
            'HardWare_Xtilt1',
            'HardWare_Xtilt2',
            'HardWare_Xtilt3',
            'HardWare_Xtilt4',
            'HardWare_Xtilt5',
            'HardWare_Xtilt6',
            'HardWare_Xtilt7',
            'HardWare_Xtilt8',
            'HardWare_Ytilt1',
            'HardWare_Ytilt2',
            'HardWare_Ytilt3',
            'HardWare_Ytilt4',
            'HardWare_Ytilt5',
            'HardWare_Ytilt6',
            'HardWare_Ytilt7',
            'HardWare_Ytilt8',
            'HardWare_SN1',
            'HardWare_SN2',
            'HardWare_SN3',
            'HardWare_SN4',
            'HardWare_SN5',
            'HardWare_SN6',
            'HardWare_SN7',
            'HardWare_SN8',
            'HardWare_Adjust',
        ]

class HardwareUpdateForm_second(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'HardWare_Autoload',
            'HardWare_Noise',
            'HardWare_PIP_X1',
            'HardWare_PIP_X2',
            'HardWare_PIP_X3',
            'HardWare_PIP_X4',
            'HardWare_PIP_X5',
            'HardWare_PIP_X6',
            'HardWare_PIP_X7',
            'HardWare_PIP_X8',
            'HardWare_PIP_Y1',
            'HardWare_PIP_Y2',
            'HardWare_PIP_Y3',
            'HardWare_PIP_Y4',
            'HardWare_PIP_Y5',
            'HardWare_PIP_Y6',
            'HardWare_PIP_Y7',
            'HardWare_PIP_Y8',
            'HardWare_PIP_Z1',
            'HardWare_PIP_Z2',
            'HardWare_PIP_Z3',
            'HardWare_PIP_Z4',
            'HardWare_PIP_Z5',
            'HardWare_PIP_Z6',
            'HardWare_PIP_Z7',
            'HardWare_PIP_Z8'
        ]
