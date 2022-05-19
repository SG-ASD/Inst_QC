from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from .decorators import Performance_ownership_required
from .forms import Performance_first
from .forms import Performance_second


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class Performance_first(UpdateView):
    model = Inspection
    form_class = Performance_first
    template_name = 'Performanceapp/Performance_Verification_first.html'
    context_object_name = 'target_Performance_first'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(Performance_first, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("Performanceapp:update_Performance2", kwargs={"Instrument_SN": self.object})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
@method_decorator(Performance_ownership_required, 'get')
class Performance_second(UpdateView):
    model = Inspection
    form_class = Performance_second
    template_name = 'Performanceapp/Performance_Verification_second.html'
    context_object_name = 'target_Performance_second'



    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(Performance_second, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("Attachmentapp:update_Attachment", kwargs={"Instrument_SN": self.object})

