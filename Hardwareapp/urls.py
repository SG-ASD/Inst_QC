from django.urls import path, include

from .views import HardwareUpdateView_first
from .views import HardwareUpdateView_second

app_name = "Hardwareapp"

urlpatterns = [
    path('hardware_first/<str:Instrument_SN>/', HardwareUpdateView_first.as_view(), name='hardware_first'),
    path('hardware_second/<str:Instrument_SN>/', HardwareUpdateView_second.as_view(), name='hardware_second'),
]