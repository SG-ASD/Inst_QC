from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from .forms import AttachmentUpdateForm
has_ownership = [User_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AttachmentUpdateView(UpdateView):
    model = Inspection
    form_class = AttachmentUpdateForm
    template_name = 'Attachmentapp/update.html'
    context_object_name = 'target_Attachment'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AttachmentUpdateView, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("Attachmentapp:update", kwargs={"Instrument_SN": self.object})

    def content_file_name(instance, filename):
        name, ext = filename.split('.')
        file_path = '{account_id}/photos/user_{user_id}.{ext}'.format(
            account_id=instance.account_id, user_id=instance.id, ext=ext)
        return file_path
