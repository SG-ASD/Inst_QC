from django.forms import ModelForm

from Inspectionapp.models import Inspection


class AppearanceUpdateForm(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Appearance_Shock_Watch',
            'Appearance_Binding',
            'Appearance_Labels',
            'Appearance_Packaging_Box',
            'Appearance_Wooden_Pallet',
            'Appearance_Transport_Jig',
            'Appearance_Shock_Watch_Image',
            'Appearance_Binding_Image',
            'Appearance_Labels_Image',
            'Appearance_Packaging_Box_Image',
            'Appearance_Wooden_Pallet_Image',
            'Appearance_Transport_Jig_Image',
            'Appearance_Video',
        ]


class AppearanceUnpackingForm(ModelForm):
    class Meta:
        model = Inspection
        fields = [
            'Appearance_Front',
            'Appearance_Top',
            'Appearance_Right',
            'Appearance_Left',
            'Appearance_Back',
            'Appearance_Acc_Damage',
            'Appearance_Acc_Missing',
        ]