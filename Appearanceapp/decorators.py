from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from Inspectionapp.models import Inspection


def Appearance_ownership_required(func):
    def decorated(request, *args, **kwargs):
        appearance = Inspection.objects.get(Instrument_SN=kwargs['Instrument_SN'])
        # if not inspection.writer == request.user:
        #     return HttpResponseForbidden()
        str = appearance.Appearance_Shock_Watch

        return func(request, *args, **kwargs)
    return decorated