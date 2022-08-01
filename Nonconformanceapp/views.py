from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from Userapp.decorators import User_ownership_required
from .models import Nonconformance
from .forms import NonconformanceUpdateForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class NonconformanceUpdateView(UpdateView):
    model = Nonconformance
    form_class = NonconformanceUpdateForm
    template_name = 'Nonconformanceapp/Non_Report.html'
    context_object_name = 'target_Nonconformance'

    def get_object(self):
        print("화면 이동")
        object = get_object_or_404(Nonconformance, Instrument_SN=self.kwargs['Instrument_SN'])
        return object


    # def get_success_url(self):
    #     object_Inspection = get_object_or_404(Nonconformance, Instrument_SN=self.kwargs['Instrument_SN'])
    #     Instrument_SN = self.request.POST.get("Instrument_SN")
    #
    #     if Start_Date == "":
    #         return reverse("Inspectionapp:update", kwargs={"Instrument_SN": self.object})

