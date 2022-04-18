from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, UpdateView

from Inspectionapp.decorators import Inspection_ownership_required
from Userapp.decorators import User_ownership_required
from Inspectionapp.models import Inspection
from Inspectionapp.forms import InspectionUpdateForm

@method_decorator(Inspection_ownership_required, 'get')
@method_decorator(Inspection_ownership_required, 'post')
class InspectionUpdateView(UpdateView):
    model = Inspection
    context_object_name = 'target_Inspection'
    form_class = InspectionUpdateForm
    success_url = reverse_lazy('Mainapp:index')

    template_name = 'Inspectionapp/update.html'

    def get_success_url(self):
        return reverse('Mainapp:index', kwargs={'instrument_SN': self.object.instrument_SN})



# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# def create(request):
#     temp_Inspection = Inspection()
#     temp_Inspection = request.POST['Instrument_SN']
#     temp_Inspection.save()
#     return redirect('Mainapp:index')



