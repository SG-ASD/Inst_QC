from django.forms import ModelForm

from Inspectionapp.models import Inspection


class AttachmentUpdateForm(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Attachment_CoverSafety_Report',
            'Attachment_Barcode_Report',
            'Attachment_Position_Report',
            'Attachment_Declaration_HHS',
            'Attachment_Declaration',
            'Attachment_Measurement_Protocol',
            'Attachment_ElectricalSafety_Report',
            'Attachment_CoverSafety_Report_File',
            'Attachment_Barcode_Report_File',
            'Attachment_Position_Report_File',
            'Attachment_Files',
        ]
