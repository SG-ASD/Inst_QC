from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.edit import FormView
from django.shortcuts import render

from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from Userapp.decorators import User_ownership_required
from .forms import AttachmentUpdateForm

import os

# Create your views here.

has_ownership = [User_ownership_required]


@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AttachmentUpdateView(UpdateView):
    model = Inspection
    form_class = AttachmentUpdateForm
    template_name = "Attachmentapp/update.html"
    context_object_name = "target_Attachment"

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AttachmentUpdateView, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit1", kwargs={"Instrument_SN": self.object})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_SN = self.kwargs.get("Instrument_SN")

        if request.method == 'POST':
            form = AttachmentUpdateForm(request.POST)
            files = request.FILES.getlist('Attachment_Files')

            if form.is_valid():
                path = os.path.join(os.getcwd(), 'media', instrument_SN)  # 파일 생성 경로
                os.makedirs(path, exist_ok=True)  # 디렉토리 생성
                file_name = []

                for idx, f in enumerate(files):
                    f.name = f"Attachment_{idx + 1}.jpg"
                    tmp = open(os.path.join(path, f.name), 'wb+')
                    file_name.append(f.name)
                    for chunk in f.chunks():
                        tmp.write(chunk)

                form_instance = get_object_or_404(Inspection, Instrument_SN=instrument_SN)
                form_instance.Attachment_CoverSafety_Report = request.POST.get('Attachment_CoverSafety_Report')
                form_instance.Attachment_Barcode_Report = request.POST.get('Attachment_Barcode_Report')
                form_instance.Attachment_Position_Report = request.POST.get('Attachment_Position_Report')
                form_instance.Attachment_Declaration_HHS = request.POST.get('Attachment_Declaration_HHS')
                form_instance.Attachment_Declaration = request.POST.get('Attachment_Declaration')
                form_instance.Attachment_Measurement_Protocol = request.POST.get('Attachment_Measurement_Protocol')
                form_instance.Attachment_ElectricalSafety_Report = request.POST.get('Attachment_ElectricalSafety_Report')

                file_name = ', '.join(file_name)
                form_instance.Attachment_Files = file_name
                form_instance.save()

                return redirect("Appearanceapp:update_Packaging", instrument_SN)
            else:
                return redirect("Attachmentapp:update_Attachment", instrument_SN)

        # instrument_SN = self.kwargs.get("Instrument_SN")
        #
        # print(f"instrument_SN:{instrument_SN}")  ############################
        #
        # if request.method == 'POST':
        #     # form_class = self.get_form_class()
        #     # form = self.get_form(form_class)
        #     form = AttachmentUpdateForm(request.POST)
        #
        #     print(f"self.models:{self.model}")  ############################
        #     # print(f"Instrument_SN:{self.model.Instrument_SN_id}")  ############################
        #     # print(f"form:{form}")  ############################
        #
        #     files = request.FILES.getlist('Attachment_Files')
        #
        #     print(f"files:{files}")  ############################
        #     print(f"form.is_valid:{form.is_valid()}")  ############################
        #
        #     if form.is_valid():
        #         print(f"request.POST.get('Instrument_SN'):{request.POST.get('Instrument_SN')}")
        #         form.save(Instrument_SN=request.POST.get('Instrument_SN'))
        #
        #         path = os.path.join(os.getcwd(), 'media', instrument_SN)  # 파일 생성 경로
        #         os.makedirs(path, exist_ok=True)  # 디렉토리 생성
        #
        #         print(f"path:{path}")  ############################
        #
        #         for idx, f in enumerate(files):
        #             instance = form.save(commit=False)
        #             instance.save()
        #
        #             f.name = f"Attachment_{idx + 1}.jpg"
        #             tmp = open(os.path.join(path, f.name), 'wb+')
        #             for chunk in f.chunks():
        #                 tmp.write(chunk)
        #         # return self.form_valid(form)
        #         return redirect("Appearanceapp:update_Packaging", instrument_SN)
        #     else:
        #         return redirect("Attachmentapp:update_Attachment", instrument_SN)

    # @transaction.atomic
    # def post(self, request, *args, **kwargs):
    #     print(f"self.get_object().Instrument_SN:{self.get_object().Instrument_SN}")  # Instrument object (D100)
    #     print(f"type:{type(self.get_object().Instrument_SN)}")  # <class 'Instrumentapp.models.Instrument'>
    #
    #     print(f"self.get_object().Instrument_SN_id:{self.get_object().Instrument_SN_id}")  # D100
    #     print(f"type:{type(self.get_object().Instrument_SN_id)}")  # <class 'str'>
    #
    #     print(f"self.get_object():{self.get_object()}")  # D100
    #     print(f"type:{type(self.get_object())}")  # <class 'Inspectionapp.models.Inspection'>
    #
    #     print(f"request.POST.get('Instrument_SN'):{request.POST.get('Instrument_SN')}")  # D100
    #     print(f"request.POST:{request.POST}")
    #
    #     # print(f"request.Instrument_SN:{request.Instrument_SN}")
    #
    #     Instrument_SN = self.get_object().Instrument_SN
    #     if request.method == 'POST':
    #         form = AttachmentUpdateForm(request.POST)
    #         file_form = AttachmentFileForm(request.POST, request.FILES)
    #         files = request.FILES.getlist('Attachment_Files')  # field name in model
    #
    #         if form.is_valid() and file_form.is_valid():
    #             form_instance = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
    #             # form_instance = form.save(commit=False)
    #             # form_instance = Inspection(Instrument_SN=Instrument_SN)
    #             form_instance.Instrument_SN = Instrument_SN
    #             form_instance.Attachment_CoverSafety_Report = request.POST.get('Attachment_CoverSafety_Report')
    #             form_instance.Attachment_Barcode_Report = request.POST.get('Attachment_Barcode_Report')
    #             form_instance.Attachment_Position_Report = request.POST.get('Attachment_Position_Report')
    #             form_instance.Attachment_Declaration_HHS = request.POST.get('Attachment_Declaration_HHS')
    #             form_instance.Attachment_Declaration = request.POST.get('Attachment_Declaration')
    #             form_instance.Attachment_Measurement_Protocol = request.POST.get('Attachment_Measurement_Protocol')
    #             # form_instance.Attachment_CoverSafety_Report_File = files
    #             form_instance.save()
    #
    #             for f in files:
    #                 file_instance = Inspection_File(Attachment_Files=f, Instrument_SN=form_instance)
    #                 file_instance.save()
    #             return redirect("Appearanceapp:update_Packaging", self.get_object().Instrument_SN_id)
    #         else:
    #             form = AttachmentUpdateForm()
    #             file_form = AttachmentFileForm()
    #         return redirect("Appearanceapp:update_Packaging", self.get_object().Instrument_SN_id)



        # instrument_SN = self.kwargs.get("Instrument_SN")
        #
        # print(f"instrument_SN:{instrument_SN}")  ############################
        #
        # # form_class = self.get_form_class()
        # # form = self.get_form(form_class)
        # form = AttachmentUpdateForm(request.POST)
        #
        # print(f"self.models:{self.model}")  ############################
        # print(f"Instrument_SN:{self.model.Instrument_SN_id}")  ############################
        # print(f"form:{form}")  ############################
        #
        # files = request.FILES.getlist('Attachment_Files')
        #
        # print(f"files:{files}")  ############################
        # print(f"form.is_valid:{form.is_valid()}")  ############################
        #
        # if form.is_valid():
        #
        #
        #
        #     path = os.path.join(os.getcwd(), 'media', instrument_SN)  # 파일 생성 경로
        #     os.makedirs(path, exist_ok=True)  # 디렉토리 생성
        #
        #     print(f"path:{path}")  ############################
        #
        #     for idx, f in enumerate(files):
        #
        #         instance = form.save(commit=False)
        #         instance.save()
        #
        #         f.name = f"Attachment_{idx + 1}.jpg"
        #         tmp = open(os.path.join(path, f.name), 'wb+')
        #         for chunk in f.chunks():
        #             tmp.write(chunk)
        #     return self.form_valid(form)
        #     # return redirect("Appearanceapp:update_Packaging", instrument_SN)
        # else:
        #     return redirect("Attachmentapp:update_Attachment", instrument_SN)
