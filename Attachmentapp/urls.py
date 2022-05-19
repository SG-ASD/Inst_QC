from django.urls import path, include

from Attachmentapp.views import AttachmentUpdateView

app_name = "Attachmentapp"

urlpatterns = [
    path('update/Attachment/<str:Instrument_SN>/', AttachmentUpdateView.as_view(), name='update_Attachment'),
]