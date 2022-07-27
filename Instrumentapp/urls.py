from django.urls import path, include
from . import views
app_name = "Instrumentapp"


urlpatterns = [
    path("<str:category>/<str:instrument_name>", views.InstrumentListView.as_view(), name="instrument"),
]
