from django.forms import ModelForm

from .models import FinishInspection


class Finished_Inspection_first(ModelForm):
    class Meta:
        model = FinishInspection
        fields =['Computer_SN',
                 'Barcode_Scanner',
                 'Inspector',
                 'Completed_Date',
                 'SW_Version',
                 'SL_Version',
                 ]

class Finished_Inspection_second(ModelForm):
    class Meta:
        model = FinishInspection
        fields =['Computer_Version',
                 'SL_Install',
                 'Method_Import',
                 'SL_Run_Version',
                 'SL_Maintenance_Screen',
                 'SL_Home_Screen',
                 'SL_mode',
                 'SL_Protocol',
                 'SL_Setting_Screen',
                 'SL_Trace',
                 'Condition',
                 'HHS_Labeled',
                 'Acc_Labeled',
                 'Labeling_Instruction_Rev',
                 'Labeling_Instruction',
                 'Labeling_Box',
                 'Label_SN',
                 'Label_MFG',
                 'Label_Option',
                 'UDI_Barcode',
                 'UDI_HRI',
                 ]