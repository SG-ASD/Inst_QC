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
        print(f"type(SN) : {type(SN)}")  # <class 'str'>
        print(f"SN : {SN}")  # G002

        temp = Inspection.objects.get(Instrument_SN=SN)
        print(f"type(temp) : {type(temp)}")  # <class 'Inspectionapp.models.Inspection'>
        print(f"temp : {temp}")  # G002

        print(f"type(temp.Instrument_SN_id) : {type(temp.Instrument_SN_id)}")  # <class 'str'>
        print(f"SN_id : {temp.Instrument_SN_id}")  # G002

        instrument_info = Inspection.objects.filter(Instrument_SN=temp.Instrument_SN_id).values()
        print(f"instrument_info : {instrument_info}")

        return instrument_info

    # def get_object(self, queryset=None):  # object 하나
    #     return self.request.  # 현재 유저를 return



    # def get_success_url(self):
    #     return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})

# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# def create(request):
#     temp_Inspection = Inspection()
#     temp_Inspection = request.POST['Instrument_SN']
#     temp_Inspection.save()
#     return redirect('Mainapp:index')



