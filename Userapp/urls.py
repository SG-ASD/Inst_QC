from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path, include

from Userapp.views import UserCreateView, UserDetailView, UserUpdateView, UserDeleteView

app_name = "Userapp"

urlpatterns = [
    path('login/', LoginView.as_view(template_name='Userapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    path('create/', UserCreateView.as_view(), name='create'),
    path('detail/<int:pk>', UserDetailView.as_view(), name='detail'),
    path('update/<int:pk>', UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', UserDeleteView.as_view(), name='delete'),
]
