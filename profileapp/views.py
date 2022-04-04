from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from profileapp.forms import ProfileCreationForm
from .models import Profile

class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    success_url = reverse_lazy('Userapp:login')
    template_name = 'profileapp/create.html'
