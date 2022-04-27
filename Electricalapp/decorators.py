from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from Inspectionapp.models import Inspection


def Electrical_ownership_required(func):
    def decorated(request, *args, **kwargs):
        electrical = Inspection.objects.get(Instrument_SN=kwargs['Instrument_SN'])

        return func(request, *args, **kwargs)
    return decorated
