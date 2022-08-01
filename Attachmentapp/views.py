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
from QC_util import Util
import os

# Create your views here.

has_ownership = [User_ownership_required]

# 설명 : Seegene STARlet Attachment 업데이트 뷰 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
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

            if form.is_valid():  # 폼이 유효하면
                # db에 값 저장
                form_instance = get_object_or_404(Inspection, Instrument_SN=instrument_SN)  # 현재 Inspection 인스턴스를 불러온다.

                if request.POST.get('Attachment_CoverSafety_Report') is None:
                    temp1 = ""
                else:
                    temp1 = request.POST.get('Attachment_CoverSafety_Report')
                if request.POST.get('Attachment_Barcode_Report') is None:
                    temp2 = ""
                else:
                    temp2 = request.POST.get('Attachment_Barcode_Report')
                if request.POST.get('Attachment_Position_Report') is None:
                    temp3 = ""
                else:
                    temp3 = request.POST.get('Attachment_Position_Report')
                if request.POST.get('Attachment_Declaration_HHS') is None:
                    temp4 = ""
                else:
                    temp4 = request.POST.get('Attachment_Declaration_HHS')
                if request.POST.get('Attachment_Declaration') is None:
                    temp5 = ""
                else:
                    temp5 = request.POST.get('Attachment_Declaration')
                if request.POST.get('Attachment_Measurement_Protocol') is None:
                    temp6 = ""
                else:
                    temp6 = request.POST.get('Attachment_Measurement_Protocol')
                if request.POST.get('Attachment_ElectricalSafety_Report') is None:
                    temp7 = ""
                else:
                    temp7 = request.POST.get('Attachment_ElectricalSafety_Report')
                form_instance.Attachment_CoverSafety_Report = temp1
                form_instance.Attachment_Barcode_Report = temp2
                form_instance.Attachment_Position_Report = temp3
                form_instance.Attachment_Declaration_HHS = temp4
                form_instance.Attachment_Declaration = temp5
                form_instance.Attachment_Measurement_Protocol = temp6
                form_instance.Attachment_ElectricalSafety_Report = temp7

                # 파일 upload
                NAS_path = r"\home\windows\품질관리_장비inspection\01 검사 성적서 관리\2022 검사 성적서\QC SW 테스트"  # NAS 폴더 경로
                path = NAS_path + '\\' + instrument_SN
                path = path.replace('\\', '/')

                if request.FILES.getlist('Attachment_CoverSafety_Report_File'):
                    CoverSafety_files = request.FILES.getlist('Attachment_CoverSafety_Report_File')
                    CoverSafety_files_name = Util.upload_files(self, CoverSafety_files, path, 'Cover Safety Verification Report', False)
                    form_instance.Attachment_CoverSafety_Report_File = CoverSafety_files_name
                else:
                    form_instance.Attachment_CoverSafety_Report_File = ""

                if request.FILES.getlist('Attachment_Barcode_Report_File'):
                    Barcode_files = request.FILES.getlist('Attachment_Barcode_Report_File')
                    Barcode_files_name = Util.upload_files(self, Barcode_files, path, 'Barcode Verification Report', False)
                    form_instance.Attachment_Barcode_Report_File = Barcode_files_name
                else:
                    form_instance.Attachment_Barcode_Report_File = ""

                if request.FILES.getlist('Attachment_Position_Report_File'):
                    Position_files = request.FILES.getlist('Attachment_Position_Report_File')
                    Position_files_name = Util.upload_files(self, Position_files, path, 'Position Verification Report', False)
                    form_instance.Attachment_Position_Report_File = Position_files_name
                else:
                    form_instance.Attachment_Position_Report_File = ""

                if request.FILES.getlist('Attachment_Files'):
                    Attachment_files = request.FILES.getlist('Attachment_Files')
                    Attachment_files_name = Util.upload_files(self, Attachment_files, path, 'Attachment', False)
                    form_instance.Attachment_Files = Attachment_files_name
                else:
                    form_instance.Attachment_Files = ""

                form_instance.save()

                return redirect('AccesorieKitapp:update_AccKit1', instrument_SN)
            else:
                return redirect('Attachmentapp:update_Attachment', instrument_SN)
