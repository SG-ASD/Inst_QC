from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView

from Userapp.decorators import User_ownership_required
from Userapp.forms import UserUpdateForm

has_ownership = [User_ownership_required]

class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('Userapp:login')
    template_name = 'Userapp/create.html'

class UserDetailView(DetailView):
    model = User
    context_object_name = 'target_user'
    template_name = 'Userapp/detail.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('Userapp:login')
    template_name = 'Userapp/update.html'

@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('Userapp:login')
    template_name = 'Userapp/delete.html'