
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from .forms import AccList1_UpdateForm, AccList2_UpdateForm, AccList3_UpdateForm
from .models import Accessories


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_first(UpdateView):
    model = Accessories
    form_class = AccList1_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_first.html'
    context_object_name = 'target_Acc_first'


    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_first, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit2", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_second(UpdateView):
    model = Accessories
    form_class = AccList2_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_second.html'
    context_object_name = 'target_Acc_second'


    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_second, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit3", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_third(UpdateView):
    model = Accessories
    form_class = AccList3_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_third.html'
    context_object_name = 'target_Acc_third'


    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_third, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit3", kwargs={"Instrument_SN": self.object.Instrument_SN_id})