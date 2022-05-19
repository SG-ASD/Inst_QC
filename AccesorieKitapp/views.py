from audioop import reverse

from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from .forms import AccList_UpdateForm
from .models import Accessories


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_first(UpdateView):
    model = Accessories
    form_class = AccList_UpdateForm
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
        return reverse("AccesorieKitapp:AccKitUpdateView_first", kwargs={"Instrument_SN": self.object})
