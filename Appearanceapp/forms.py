from django.forms import ModelForm

from Appearanceapp.models import Appearance


class AppearanceCreationForm(ModelForm):
    class Meta:
        model = Appearance
        fields = ['Instrument_SN', 'Shock_Watch', 'Binding', 'Labels', 'Packaging_Box', 'Wooden_Pallet','Transport_Jig',
        'Shock_Watch_Image', 'Binding_Image', 'Labels_Image', 'Packaging_Box_Image', 'Wooden_Pallet_Image', 'Transport_Jig_Image', 'Video']
