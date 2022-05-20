from django.forms import ModelForm

from AccesorieKitapp.models import Accessories


class AccList1_UpdateForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ['Unpack_Instructions',
                  'Installation_Qualification',
                  'Final_Configuation',
                  'Measurement_Protocol',
                  'EU_Declaration',
                  'Declaration_Quality',
                  'Packing_Checklist',
                  'Maintenance',
                  'DeclarationSTARlet',
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

class AccList2_UpdateForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ['Sensor_4L',
                  'Solid_Waste',
                  'USB_Liquid',
                  'USB_Solid_Liquid',
                  'USB_Venus',
                  'Eppendorf',
                  'Core_Gripper',
                  'Needle_Check',
                  'Needle_Lot',
                  'Separator',
                  'Tip_Eject',
                  'Power_Cord7',
                  'Power_CordP',
                  'Cable_USB',
                  'Fuse',
                  'Screw',
                  'Fitting',
                  'Liq_Waste',
                  ]

class AccList3_UpdateForm(ModelForm):
    class Meta:
        model = Accessories
        fields = ['XArm',
                  'Bar_Left',
                  'Bar_Top',
                  'Bag',
                  'Tube_32',
                  'TipRack_5',
                  'MFX4',
                  'SEEG',
                  'FLHX',
                  'SOHX',
                  'HHS_Plate',
                  'MTP',
                  'Verify_Kit',
                  'STD',
                  'High',
                  'HHS_SN',
                  'HHS_Check',
                  'HHS_Manual',
                  'Stop_Barcode',
                  'Remark',
                  ]