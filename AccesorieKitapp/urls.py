from django.urls import path, include

from AccesorieKitapp.views import AccKitUpdateView_first, AccKitUpdateView_second, AccKitUpdateView_third

app_name = "AccesorieKitapp"

urlpatterns = [
    path('update/AccKit1/<str:Instrument_SN>/', AccKitUpdateView_first.as_view(), name='update_AccKit1'),
    path('update/AccKit2/<str:Instrument_SN>/', AccKitUpdateView_second.as_view(), name='update_AccKit2'),
    path('update/AccKit3/<str:Instrument_SN>/', AccKitUpdateView_third.as_view(), name='update_AccKit3'),
]



