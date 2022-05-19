from django.urls import path, include

from AccesorieKitapp.views import AccKitUpdateView_first

app_name = "AccesorieKitapp"

urlpatterns = [
    path('update/Acckit1/<str:Instrument_SN>/', AccKitUpdateView_first.as_view(), name='update_AccKit1'),
    # path('update/Acckit2/<str:Instrument_SN>/', AccKitUpdateView_second.as_view(), name='update_AccKit2'),
    # path('update/Acckit3/<str:Instrument_SN>/', AccKitUpdateView_third.as_view(), name='update_AccKit3'),
]



