from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection
from Userapp.decorators import User_ownership_required
from Appearanceapp.forms import AppearanceUpdateForm

has_ownership = [User_ownership_required]

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AppearanceUpdateView(UpdateView):
    model = Inspection
    context_object_name = 'target_Appearance'
    form_class = AppearanceUpdateForm
    success_url = reverse_lazy('Mainapp:index')

    template_name = 'Appearanceapp/update.html'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    def form_valid(self, form):
        temp_Appearance = form.save(commit=False)
        temp_Appearance.user = self.request.user
        temp_Appearance.save()
        return super().form_valid(form)