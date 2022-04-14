from django.urls import path, include
from . import views

urlpatterns = [
    path("<str:category>/<str:instrument_name>", views.InstrumentListView.as_view(), name="instrument"),
    # path("<str:category>/add", views.InstrumentCreateView.as_view(), name="add_instrument"),
]
