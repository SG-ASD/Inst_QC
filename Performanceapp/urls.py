from django.urls import path

from .views import Performance_first, Performance_second

app_name = 'Performanceapp'

urlpatterns = [
    path('Performance1/<str:Instrument_SN>/', Performance_first.as_view(), name='update_Performance1'),
    path('Performance2/<str:Instrument_SN>/', Performance_second.as_view(), name='update_Performance2'),
]
