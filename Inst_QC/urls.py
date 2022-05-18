"""Inst_QC URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('Mainapp.urls')),
    path("User/", include('Userapp.urls')),
    path('profile/', include('profileapp.urls')),
    path("", include('Instrumentapp.urls')),
    path("Inspection/", include('Inspectionapp.urls')),
    path("Appearance/", include('Appearanceapp.urls')),
    path("Electrical/", include('Electricalapp.urls')),
    path("Hardware/", include('Hardwareapp.urls')),
    path("Performance/", include('Performanceapp.urls')),
    path("Attachment/", include('Attachmentapp.urls')),
    path("AccesorieKit/", include('AccesorieKitapp.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
