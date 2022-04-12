from django.forms import ModelForm

from Inspectionapp.models import Inspection


class InspectionCreationForm(ModelForm):
    class Meta:
        model = Inspection
        fields = ['Instrument_SN', 'Inspector', 'Computer_SN', 'Revision', 'Start_Date', 'Completed_Date','SW_Version',
                    'FV2_Version', 'FW_PipetteCh', 'FW_Xdrive', 'FW_Master']




