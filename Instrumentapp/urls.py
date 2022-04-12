from django.urls import path, include
from . import views

urlpatterns = [
    path("<str:category>/<str:instrument_name>", views.Instrument_View.as_view(), name="instrument"),
]
