from django.forms import ModelForm, ClearableFileInput
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

    # def save(self, **kwargs):
    #     post = super().save(commit=False)
    #     post.Instrument_SN = kwargs.get('Instrument_SN', None)
    #     post.save()
    #
    #     return post


# class AttachmentFileForm(ModelForm):
#     class Meta:
#         model = Inspection_File
#         fields = [
#             'Attachment_Files'
#         ]
#         # widget is important to upload multiple files
#         widgets = {
#             'Attachment_Files': ClearableFileInput(attrs={'multiple': True}),
#         }
