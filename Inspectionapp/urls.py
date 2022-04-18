from django.urls import path, include
from . import views
app_name = "Inspectionapp"

urlpatterns = [
    path('<str:SN>', views.InspectionCreateView.as_view(), name='update'),
]