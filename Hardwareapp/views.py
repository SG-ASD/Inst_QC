import os
from datetime import date, timedelta
from urllib.parse import quote

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
        Start_Date = context['object'].Start_Date
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_calibration"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Equipment_Name__contains='Channel Calibration Tool').\
            filter(CAL_Date__lte=Start_Date, Expiration_Date__gte=Start_Date)
        context["inspection_Barcode"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Equipment_Name__contains='Barcode Carrier').\
            filter(CAL_Date__lte=Start_Date, Expiration_Date__gte=Start_Date)
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
    print("1")
    # df = pd.DataFrame([
    #                     [100,110,120],
    #                     [200,210,220],
    #                     [300, 310, 320],
    #                     ])
    filepath = 'D:\\QC_Software\\QC Software\\Seegene STARlet\\G230\\Traces\\Adjust_Arm_Z_using_PIP_SN_G230.trc'
    # filename = os.path.basename(filepath)
    # encoded_filename = quote(filename)
    # with open(filepath, 'rb') as f:
    #     response = HttpResponse(f, content_type='application/vnd.ms-excel')
    #
    #
    #     response['Content-Disposition'] = "attachment; filename*=utf-8''{}".format(encoded_filename)
    # return response
    # io = StringIO
    # df.to_csv(io)
    # io.seek(0)
    # response = HttpResponse(io, content='text/csv')
    # response['Content-Disposition'] = "attachment; filename*=utf-f''{}".format(encoded_filename)
    # import tkinter
    # from tkinter import filedialog
    #
    # root = tkinter.Tk()
    # root.withdraw()
    # dir_path = filedialog.askdirectory(parent=root, initialdir="/", title='Please select a directory')
    # print("\ndir_path : ", dir_path)
    #
    # # return response
    # return resolve_url("Hardwareapp:update_Hardware1", Instrument_SN=Instrument_SN)