from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView
from Userapp.decorators import User_ownership_required
from Inspectionapp.models import Inspection
from Inspectionapp.forms import InspectionCreationForm

has_ownership = [User_ownership_required]
class InspectionCreateView(CreateView):
    model = Inspection
    context_object_name = 'target_Inspection'
    form_class = InspectionCreationForm
    success_url = reverse_lazy('Mainapp:index')

    template_name = 'Inspectionapp/create.html'

    def create(request):
        temp_Inspection = Inspection()
        temp_Inspection = request.POST['Instrument_SN']
        # temp_Inspector = request.POST['Inspector']
        temp_Inspection.save()
        return redirect('Mainapp:index')

    # def form_valid(self, form):
    #     temp_inspection = form.save(commit=False)
    #     temp_inspection.user = self.request.user
    #     temp_inspection.save()
    #     return super().form_valid(form)




# @method_decorator(has_ownership, 'get')
# @method_decorator(has_ownership, 'post')
# def create(request):
#     temp_Inspection = Inspection()
#     temp_Inspection = request.POST['Instrument_SN']
#     temp_Inspection.save()
#     return redirect('Mainapp:index')



