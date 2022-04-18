from django.urls import path, include

from .views import InspectionUpdateView

app_name = "Inspectionapp"

urlpatterns = [
    path('update/<str:SN>', InspectionUpdateView.as_view(), name='update'),
]