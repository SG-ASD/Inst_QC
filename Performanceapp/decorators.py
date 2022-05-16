from django.contrib.auth.models import User
from django.http import HttpResponseForbidden

from Inspectionapp.models import Inspection


def Performance_ownership_required(func):
    def decorated(request, *args, **kwargs):
        electrical = Inspection.objects.get(Instrument_SN=kwargs['Instrument_SN'])

        date = request.GET.get('trip-start')
        print("HTML에서 넘어온 date: ", date)
        context = {
            'date': date,
        }

        return func(request, *args, **kwargs)
    return decorated

