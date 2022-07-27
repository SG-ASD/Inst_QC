from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from Instrumentapp.models import Version, Revision
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
        Start_Date = self.request.POST.get("Start_Date")
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(InspectionUpdateView, self).get_context_data(**kwargs)
        Instrument_Nm = context['object'].Name
        Start_Date = context['object'].Start_Date
        context["Hamilton_SW_Ver"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Hamilton S/W Version').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Hamilton_FV2_Ver"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Hamilton FV2 Version').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Hamilton_Pipette_Ch"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Pipette Ch (PX)').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Hamilton_X_Drive"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='X-drive (XO)').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Hamilton_Master_CO"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Master (CO)'). \
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Document_No"] = Revision.objects.filter(Instrument_Name=Instrument_Nm).filter(Type__contains='수입검사 성적서'). \
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)

        return context


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
