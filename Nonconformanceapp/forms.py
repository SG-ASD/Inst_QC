from django.forms import ModelForm

from .models import Nonconformance


class NonconformanceUpdateForm(ModelForm):
    class Meta:
        model = Nonconformance
        fields = [
            'Instrument_SN',
            'Computer_SN',
            'Name',
            'Inspector',
            'Start_Date',
            'Doc_Num',
            'Revision',
            'Issue_Num',
            'Category',
            'Attachment',
        ]
