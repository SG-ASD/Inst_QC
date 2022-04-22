from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Appearanceapp.decorators import Appearance_ownership_required
from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from Appearanceapp.forms import AppearanceUpdateForm

has_ownership = [login_required, Appearance_ownership_required]

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
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
        context["inspection_subcategory"] = Inspection_Category.objects.distinct().values_list('Subcategory', flat=True)
        print(f"context : {context}")
        return context

    def get_success_url(self):
        # return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})
        return reverse("Appearanceapp:update", kwargs={"Instrument_SN": self.object})


    # def form_valid(self, form):
    #     temp_Appearance = form.save(commit=False)
    #     temp_Appearance.user = self.request.user
    #     temp_Appearance.save()
    #     return super().form_valid(form)
