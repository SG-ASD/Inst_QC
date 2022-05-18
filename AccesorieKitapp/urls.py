from django.urls import path, include

from AccesorieKitapp.views import AccKitUpdateView_first

app_name = "AccesorieKitapp"

urlpatterns = [
    path('acckit_first/<str:Instrument_SN>/', AccKitUpdateView_first.as_view(), name='AccKit_first'),
]



