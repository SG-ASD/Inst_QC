from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from Inspectionapp.models import Inspection


def Inspection_ownership_required(func):
    def decorated(request, *args, **kwargs):
        inspection = Inspection.objects.get(Instrument_SN=kwargs['Instrument_SN'])
        # if not inspection.writer == request.user:
        #     return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated