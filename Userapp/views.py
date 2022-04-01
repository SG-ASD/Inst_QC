from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView
from Userapp.forms import UserUpdateForm


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('Userapp:login')
    template_name = 'Userapp/create.html'

class UserDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'Userapp/detail.html'

class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('Userapp:login')
    template_name = 'Userapp/update.html'