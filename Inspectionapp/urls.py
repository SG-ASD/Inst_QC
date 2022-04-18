from django.urls import path, include

from Inspectionapp.views import InspectionUpdateView

app_name = "Inspectionapp"

urlpatterns = [
    path('update/<int:pk>/', InspectionUpdateView.as_view(), name='update'),
]