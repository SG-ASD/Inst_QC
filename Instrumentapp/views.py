from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Instrument

# Create your views here.


class IndexView(ListView):
    model = Instrument
    template_name = "Instrumentapp/instrument.html"
    context_object_name = "main_category"
    # context_object_name = "reviews"
    # paginate_by = 4
    # ordering = ["-dt_created"]
