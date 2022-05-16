from datetime import date, timedelta

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.db.models.functions import datetime
from django.shortcuts import render, get_object_or_404

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
        context["inspection_calibration"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Description__contains='Channel Calibration Tool').\
            filter(CalibrationDt__lte=date.today(), ValidationDt__gte=date.today())
        context["inspection_Barcode"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Description__contains='Barcode Carrier').\
            filter(CalibrationDt__lte=date.today(), ValidationDt__gte=date.today())
        return context

    def get_success_url(self):
        return reverse("Hardwareapp:hardware_second", kwargs={"Instrument_SN": self.object})

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
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("Performanceapp:update_Performance_first", kwargs={"Instrument_SN": self.object})
