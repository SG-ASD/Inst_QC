from django.urls import path, include

from AccesorieKitapp.views import AccKitUpdateView_first, AccKitUpdateView_second, AccKitUpdateView_third
from FinishedInspectionapp.views import FinishedInspection_UpdateView_first, FinishedInspection_UpdateView_second

app_name = "FinishedInspectionapp"

urlpatterns = [
    path('update/finishedinspection1/<str:Instrument_SN>/', FinishedInspection_UpdateView_first.as_view(), name='update_finish1'),
    path('update/finishedinspection2/<str:Instrument_SN>/', FinishedInspection_UpdateView_second.as_view(), name='update_finish2'),
]





