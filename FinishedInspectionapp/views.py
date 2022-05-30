from datetime import date

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Hardwareapp.models import Calibration
from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from .forms import Finished_Inspection_first, Finished_Inspection_second
from .models import FinishInspection

has_ownership = [User_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FinishedInspection_UpdateView_first(UpdateView):
    model = FinishInspection
    form_class = Finished_Inspection_first
    template_name = 'FinishedInspectionapp/finish_inspection_first.html'
    context_object_name = 'target_finish_first'

    def get_object(self):
        object = get_object_or_404(FinishInspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):

        context = super(FinishedInspection_UpdateView_first, self).get_context_data(**kwargs)
        Instrument_Nm = context['object'].Name
        context["inspection_calibration"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Description__contains='Barcode Scanner').\
            filter(CalibrationDt__lte=date.today(), ValidationDt__gte=date.today())
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("FinishedInspectionapp:update_finish2", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FinishedInspection_UpdateView_second(UpdateView):
    model = FinishInspection
    form_class = Finished_Inspection_second
    template_name = 'FinishedInspectionapp/finish_inspection_second.html'
    context_object_name = 'target_finish_second'

    def get_object(self):
        object = get_object_or_404(FinishInspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(FinishedInspection_UpdateView_second, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("FinishedInspectionapp:update_finish2", kwargs={"Instrument_SN": self.object.Instrument_SN_id})


