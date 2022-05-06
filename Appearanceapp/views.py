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
from .forms import AppearanceUpdateForm, AppearanceUnpackingForm

has_ownership = [User_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AppearanceUpdateView(UpdateView):
    model = Inspection
    form_class = AppearanceUpdateForm
    template_name = 'Appearanceapp/update.html'
    context_object_name = 'target_Appearance'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AppearanceUpdateView, self).get_context_data(**kwargs)
        # subcategory = self.kwargs.get("category")
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Appearance Inspection").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        # return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})
        return reverse("Appearanceapp:update_Unpacking", kwargs={"Instrument_SN": self.object})


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AppearanceUnpackingView(UpdateView):
    model = Inspection
    form_class = AppearanceUnpackingForm
    template_name = 'Appearanceapp/Unpacking_State.html'
    context_object_name = 'target_Unpacking_State'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AppearanceUnpackingView, self).get_context_data(**kwargs)
        # subcategory = self.kwargs.get("category")
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Appearance Inspection").values_list('Subcategory', flat=True)
        return context

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    def get_success_url(self):
        return reverse("Electricalapp:update", kwargs={"Instrument_SN": self.object})