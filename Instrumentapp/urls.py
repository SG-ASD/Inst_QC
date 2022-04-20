from django.urls import path, include
from . import views
app_name = "Instrumentapp"

urlpatterns = [
    path("<str:category>/<str:Instrument_SN>", views.InstrumentListView.as_view(), name="instrument"),
    # path("<str:category>/add", views.InstrumentCreateView.as_view(), name="add_instrument"),
]
