from django.forms import ModelForm

from Appearanceapp.models import Appearance


class AppearanceCreationForm(ModelForm):
    class Meta:
        model = Appearance
        fields = ['Instrument_SN', 'Shock_Watch', 'Binding', 'Labels', 'Packaging_Box', 'Wooden_Pallet','Transport_Jig']