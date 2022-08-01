from django.urls import path

from .views import NonconformanceUpdateView

app_name = "Nonconformanceapp"

urlpatterns = [
    path('update/<str:Instrument_SN>/', NonconformanceUpdateView.as_view(), name='update'),
]