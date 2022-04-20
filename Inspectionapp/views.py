from django.contrib.auth.decorators import login_required
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

has_ownership = [Inspection_ownership_required, login_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class InspectionUpdateView(UpdateView):
    model = Inspection
    form_class = InspectionUpdateForm
    template_name = 'Inspectionapp/update.html'
    pk_url_kwarg = "instrument_SN"
    context_object_name = 'target_Inspection'

    def get_object(self):
        self.object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        print(f"object : {self.object}")
        return self.object

    def get_success_url(self):
        # return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})
        print(f"success: {self.object}")
        return reverse("Appearanceapp:update", kwargs={"Instrument_SN": self.object})
