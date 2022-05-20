from django.urls import path, include

from .views import HardwareUpdateView_first
from .views import HardwareUpdateView_second

app_name = "Hardwareapp"

urlpatterns = [
    path('update/hardware1/<str:Instrument_SN>/', HardwareUpdateView_first.as_view(), name='update_Hardware1'),
    path('update/hardware2/<str:Instrument_SN>/', HardwareUpdateView_second.as_view(), name='update_Hardware2'),
]