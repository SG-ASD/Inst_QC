from django.urls import path

from .views import AppearanceUpdateView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'Appearanceapp'

urlpatterns = [
    path('update/<str:Instrument_SN>/', AppearanceUpdateView.as_view(), name='update'),
]
