from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from .decorators import Inspection_ownership_required
from Userapp.decorators import User_ownership_required
from .models import Inspection
from .forms import InspectionUpdateForm

# @method_decorator(Inspection_ownership_required, 'get')
# @method_decorator(Inspection_ownership_required, 'post')


class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionUpdateForm
    template_name = 'Inspectionapp/update.html'
    context_object_name = 'target_Inspection'
    pk_url_kwarg = "SN"
    # success_url = reverse_lazy('Mainapp:index')

    def get_queryset(self):
        SN = self.kwargs.get("SN")
        print(f"SN : {SN}")

        temp = Inspection.objects.get(Instrument_SN=SN)
        # print(Inspection.objects.get(Instrument_SN=SN))
        print(f"SN_id : {temp.Instrument_SN_id}")
        print(f"type : {type(temp.Instrument_SN_id)}")

        instrument_info = Inspection.objects.filter(Instrument_SN=temp.Instrument_SN_id).values()
        print(instrument_info)

        return instrument_info


    # def get_success_url(self):
    #     return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})

# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# def create(request):
#     temp_Inspection = Inspection()
#     temp_Inspection = request.POST['Instrument_SN']
#     temp_Inspection.save()
#     return redirect('Mainapp:index')



