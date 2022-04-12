from django.urls import path, include

from Inspectionapp.views import InspectionCreateView

app_name = "Inspectionapp"

urlpatterns = [
    path('create/', InspectionCreateView.as_view(), name='create'),
]