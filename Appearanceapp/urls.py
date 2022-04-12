from django.urls import path

from Appearanceapp.views import AppearanceCreateView
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'Appearanceapp'

urlpatterns = [
    path('create/', AppearanceCreateView.as_view(), name='create'),
]