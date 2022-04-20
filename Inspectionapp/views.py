from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView
from Userapp.decorators import User_ownership_required
from .decorators import Inspection_ownership_required
from .models import Inspection
from .forms import InspectionUpdateForm


@method_decorator(Inspection_ownership_required, 'get')
@method_decorator(Inspection_ownership_required, 'post')
class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionUpdateForm
    template_name = 'Inspectionapp/update.html'
    pk_url_kwarg = "instrument_SN"
    context_object_name = 'target_Inspection'
    # success_url = reverse_lazy('Mainapp:index')

    def get_object(self):
        self.object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        print(f"object : {self.object}")

        return self.object

    def get_success_url(self):
        # return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})
        print(f"success: {self.object}")
        return reverse("Inspectionapp:update", kwargs={"Instrument_SN": self.object})

    # @transaction.atomic
    # def post(self, request, *args, **kwargs):
    #     instrument_SN = self.kwargs.get("Instrument_SN")
    #
    #     if self.request.method == "POST":
    #         print(f"self.request.POST : {self.request.POST}")
    #         inst_name = self.request.POST.get("s1")
    #         inst_SN = self.request.POST.get("s2")
    #
    #         context = {"s2": inst_SN, "s1": inst_name}
    #
    #         # new_inst = Instrument(SN=inst_SN, Name=inst_name)
    #         # new_inst.save()
    #         # new_inspection = Inspection(Instrument_SN=new_inst.SN, Name=inst_name, Status="검사대기")
    #         # new_inspection.save()
    #
    #         new_instrument = Instrument.objects.create(
    #             SN=inst_SN,
    #             Name=inst_name
    #         )
    #
    #         new_inspection = Inspection.objects.create(
    #             Instrument_SN=new_instrument,
    #             Name=inst_name,
    #             Status="검사대기"
    #         )
    #
    #     print(f"context : {context}")
    #     print(f"category : {category}")
    #     print(f"instrument_name : {instrument_name}")
    #
    #     # return render(self.request, "instrument", {'category': category, 'instrument_name': instrument_name})
    #     return redirect("Instrumentapp:instrument", category, instrument_name)

# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# def create(request):
#     temp_Inspection = Inspection()
#     temp_Inspection = request.POST['Instrument_SN']
#     temp_Inspection.save()
#     return redirect('Mainapp:index')



