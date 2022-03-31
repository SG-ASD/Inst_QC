from django.urls import path, include

from Userapp.views import UserCreateView

app_name = "Userapp"

urlpatterns = [
    path('create/', UserCreateView.as_view(), name='create'),

]
