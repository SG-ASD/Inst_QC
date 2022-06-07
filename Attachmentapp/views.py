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
    template_name = 'Attachmentapp/update.html'
    context_object_name = 'target_Attachment'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AttachmentUpdateView, self).get_context_data(**kwargs)
        context['inspection_category'] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        return reverse('AccesorieKitapp:update_AccKit1', kwargs={'Instrument_SN': self.object})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_SN = self.kwargs.get('Instrument_SN')

        if request.method == 'POST':
            form = AttachmentUpdateForm(request.POST)  # request된 폼
            files = request.FILES.getlist('Attachment_Files')  # upload 할 파일 리스트

            if form.is_valid():  # 폼이 유효하면
                path = os.path.join(os.getcwd(), 'media', instrument_SN)  # 파일 생성 경로
                os.makedirs(path, exist_ok=True)  # 디렉토리 생성
                file_name = []

                # 파일 upload
                for idx, f in enumerate(files):
                    extension = f.name.split('.')[-1]  # 파일 확장자
                    f.name = f"Attachment_{idx + 1}.{extension}"  # 파일 이름 설정
                    tmp = open(os.path.join(path, f.name), 'wb+')  # 디렉토리에 파일 생성
                    file_name.append(f.name)
                    for chunk in f.chunks():
                        tmp.write(chunk)  # 파일 write

                # db에 값 저장
                form_instance = get_object_or_404(Inspection, Instrument_SN=instrument_SN)  # 현재 Inspection 인스턴스를 불러온다.
                form_instance.Attachment_CoverSafety_Report = request.POST.get('Attachment_CoverSafety_Report')
                form_instance.Attachment_Barcode_Report = request.POST.get('Attachment_Barcode_Report')
                form_instance.Attachment_Position_Report = request.POST.get('Attachment_Position_Report')
                form_instance.Attachment_Declaration_HHS = request.POST.get('Attachment_Declaration_HHS')
                form_instance.Attachment_Declaration = request.POST.get('Attachment_Declaration')
                form_instance.Attachment_Measurement_Protocol = request.POST.get('Attachment_Measurement_Protocol')
                form_instance.Attachment_ElectricalSafety_Report = request.POST.get('Attachment_ElectricalSafety_Report')

                file_name = ', '.join(file_name)  # 리스트를 문자열로 변환
                file_name = path + '\\' + file_name
                form_instance.Attachment_Files = file_name
                form_instance.save()

                return redirect('AccesorieKitapp:update_AccKit1', instrument_SN)
            else:
                return redirect('Attachmentapp:update_Attachment', instrument_SN)
