from django.urls import path

from Appearanceapp.views import AppearanceUpdateView, AppearanceUnpackingView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'Appearanceapp'

urlpatterns = [
    path('update/<str:Instrument_SN>/', AppearanceUpdateView.as_view(), name='update'),
    path('update_Unpacking/<str:Instrument_SN>/', AppearanceUnpackingView.as_view(), name='update_Unpacking'),
]