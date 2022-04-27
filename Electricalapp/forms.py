from django.forms import ModelForm

from Inspectionapp.models import Inspection


class ElectricalUpdateForm(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'ElectricalTest_HiPotential',
            'ElectricalTest_GroundResistance',
            'ElectricalTest_PowerSWFunction',
            'ElectricalTest_PowerLED',
        ]
