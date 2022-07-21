from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from Userapp.decorators import User_ownership_required
from .models import Inspection
from .forms import InspectionUpdateForm


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionUpdateForm
    template_name = 'Inspectionapp/update.html'
    context_object_name = 'target_Inspection'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object


    def get_success_url(self):
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        Start_Date = self.request.POST.get("Start_Date")
        CompleteDt = self.request.POST.get("CompleteDt")
        Instrument_SN = self.request.POST.get("Instrument_SN")

        if Start_Date == "":
            messages.warning(self.request, '검사 시작일을 지정해주세요.')
            return reverse("Inspectionapp:update", kwargs={"Instrument_SN": self.object})


        if Start_Date != "":
            Inspection.objects.filter(Instrument_SN=object_Inspection.Instrument_SN_id).update(Status='검사진행중')
        return reverse("Appearanceapp:update_Packaging", kwargs={"Instrument_SN": self.object})
