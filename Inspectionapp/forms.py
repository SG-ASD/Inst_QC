from django.forms import ModelForm

from .models import Inspection


class InspectionUpdateForm(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Inspector',
            'Computer_SN',
            'Revision',
            'SW_Version',
            'FV2_Version',
            'FW_PipetteCh',
            'FW_Xdrive',
            'FW_Master'
        ]




