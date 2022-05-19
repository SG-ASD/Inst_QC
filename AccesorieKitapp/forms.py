from django.forms import ModelForm

from AccesorieKitapp.models import Accessories


class AccList_UpdateForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ['Unpack_Instructions',
                  'Installation_Qualification',
                  'Final_Configuation',
                  'Measurement_Protocol',
                  'DeclarationSTARlet',
                  'MeasurementProtocolSTARlet',
                  'EU_Declaration',
                  'Declaration_Quality',
                  'Packing_Checklist',
                  'Maintenance',
                  'Channel_Adjust',
                  'Test_Report',
                  'Loading_Table',
                  'Side_Cover_right',
                  'Side_Cover_left',
                  'Rear_Piexiglas',
                  'Top_Plexiglas',
                  'Left_Plexiglas',
                  'Right_Plexiglas',
                  ]