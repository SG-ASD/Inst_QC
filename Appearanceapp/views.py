from django.shortcuts import render, redirect

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from Appearanceapp.models import Appearance
from Userapp.decorators import User_ownership_required
from Appearanceapp.forms import AppearanceCreationForm

has_ownership = [User_ownership_required]

class AppearanceCreateView(CreateView):
    model = Appearance
    context_object_name = 'target_Appearance'
    form_class = AppearanceCreationForm
    success_url = reverse_lazy('Mainapp:index')

    template_name = 'Appearanceapp/create.html'

    def form_valid(self, form):
        temp_Appearance = form.save(commit=False)
        temp_Appearance.user = self.request.user
        temp_Appearance.save()
        return super().form_valid(form)