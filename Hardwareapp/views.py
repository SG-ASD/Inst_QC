from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models.functions import datetime
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, resolve_url

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from .forms import HardwareUpdateForm_first
from .forms import HardwareUpdateForm_second
from .models import Calibration

has_ownership = [User_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class HardwareUpdateView_first(UpdateView):
    model = Inspection
    form_class = HardwareUpdateForm_first
    template_name = 'Hardwareapp/hardware_first.html'
    context_object_name = 'target_Hardware'


    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(HardwareUpdateView_first, self).get_context_data(**kwargs)
        Instrument_Nm = context['object'].Name

        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_calibration"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Equipment_Name__contains='Channel Calibration Tool').\
            filter(CAL_Date__lte=date.today(), Expiration_Date__gte=date.today())
        context["inspection_Barcode"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Equipment_Name__contains='Barcode Carrier').\
            filter(CAL_Date__lte=date.today(), Expiration_Date__gte=date.today())
        return context

    def get_success_url(self):
        return reverse("Hardwareapp:update_Hardware2", kwargs={"Instrument_SN": self.object})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class HardwareUpdateView_second(UpdateView):
    model = Inspection
    form_class = HardwareUpdateForm_second
    template_name = 'Hardwareapp/hardware_second.html'
    context_object_name = 'target_Hardware'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(HardwareUpdateView_second, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("Performanceapp:update_Performance1", kwargs={"Instrument_SN": self.object})

@login_required
def post_detail(request, Instrument_SN):
    qs = Inspection.objects.all()
    q = request.GET.get('formFile', '')
    if q:
        qs = qs.filter(message__icontains=q)
        # instagram/templetes/instagram/post_list.html
    return redirect("Hardwareapp:update_Hardware1", Instrument_SN)
    # return resolve_url("Hardwareapp:update_Hardware1", Instrument_SN=Instrument_SN)