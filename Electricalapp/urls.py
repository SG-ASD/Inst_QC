from django.urls import path

from .views import ElectricalUpdateView

app_name = 'Electricalapp'

urlpatterns = [
    path('update/<str:Instrument_SN>/', ElectricalUpdateView.as_view(), name='update'),
]
