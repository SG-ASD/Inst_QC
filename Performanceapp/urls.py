from django.urls import path

from .views import Performance_first, Performance_second

app_name = 'Performanceapp'

urlpatterns = [
    path('Performance_first/<str:Instrument_SN>/', Performance_first.as_view(), name='update_Performance_first'),
    path('Performance_second/<str:Instrument_SN>/', Performance_second.as_view(), name='update_Performance_second'),
]
