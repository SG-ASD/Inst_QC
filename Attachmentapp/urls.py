from django.urls import path, include

from Attachmentapp.views import AttachmentUpdateView

app_name = "Attachmentapp"

urlpatterns = [
    path('Attachment/<str:Instrument_SN>/', AttachmentUpdateView.as_view(), name='update'),
]