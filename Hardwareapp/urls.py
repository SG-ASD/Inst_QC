from django.urls import path, include

from .views import HardwareUpdateView_first
from .views import HardwareUpdateView_second
from . import views
app_name = "Hardwareapp"

urlpatterns = [
    path('update/Hardware1/<str:Instrument_SN>/', HardwareUpdateView_first.as_view(), name='update_Hardware1'),
    path('update/Hardware2/<str:Instrument_SN>/', HardwareUpdateView_second.as_view(), name='update_Hardware2'),
    path('update/Hardware1/<str:Instrument_SN>/post_detail/', views.post_detail,name='test'),
]