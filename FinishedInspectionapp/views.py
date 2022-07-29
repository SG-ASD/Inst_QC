from datetime import date

import openpyxl
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Hardwareapp.models import Calibration
from Inspectionapp.models import Inspection, Inspection_Category
from Instrumentapp.models import Version, Revision
from Userapp.decorators import User_ownership_required
from .forms import Finished_Inspection_first, Finished_Inspection_second
from .models import FinishInspection

has_ownership = [User_ownership_required]

# 설명 : Seegene STARlet 완제품 성적서 업데이트 뷰 첫번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FinishedInspection_UpdateView_first(UpdateView):
    model = FinishInspection
    form_class = Finished_Inspection_first
    template_name = 'FinishedInspectionapp/finish_inspection_first.html'
    context_object_name = 'target_finish_first'

    def get_object(self):
        Computer_SN = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN']).Computer_SN
        FinishInspection.objects.filter(Instrument_SN=self.kwargs['Instrument_SN']).update(Computer_SN=Computer_SN)
        object = get_object_or_404(FinishInspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(FinishedInspection_UpdateView_first, self).get_context_data(**kwargs)
        Instrument_Nm = context['object'].Name
        Start_Date = context['object'].Start_Date

        context["Hamilton_SW_Ver"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Hamilton S/W Version').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["Seegene_Launcher_Ver"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='Seegene Launcher Version').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)


        context["inspection_calibration"] = Calibration.objects.filter(Instrument=Instrument_Nm).filter(Equipment_Name__contains='Barcode Scanner').\
            filter(CAL_Date__lte=date.today(), Expiration_Date__gte=date.today())
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection"] = Inspection.objects.filter(Instrument_SN=self.kwargs['Instrument_SN'])
        return context

    def get_success_url(self):
        Start_Date = self.request.POST.get("Start_Date")

        if Start_Date == "":
            messages.warning(self.request, '검사 시작일을 지정해주세요.')
            return reverse("FinishedInspectionapp:update_finish1", kwargs={"Instrument_SN": self.object.Instrument_SN_id})
        return reverse("Inspectionapp:update", kwargs={"Instrument_SN": self.object.Instrument_SN_id})


# 설명 : Seegene STARlet 완제품 성적서 업데이트 뷰 두번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class FinishedInspection_UpdateView_second(UpdateView):
    model = FinishInspection
    form_class = Finished_Inspection_second
    template_name = 'FinishedInspectionapp/finish_inspection_second.html'
    context_object_name = 'target_finish_second'

    def get_object(self):
        object = get_object_or_404(FinishInspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(FinishedInspection_UpdateView_second, self).get_context_data(**kwargs)
        Instrument_Nm = context['object'].Name
        Start_Date = context['object'].Start_Date
        context["inspection"] = Inspection.objects.filter(Instrument_SN=self.kwargs['Instrument_SN'])
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)


        context["labeling_package_instruction"] = Revision.objects.filter(Type__contains='Labelling & Packaging Instruction').\
            filter(Start_Dt__lte=Start_Date, Expiry_Dt__gte=Start_Date)
        context["inst_label"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='장비 라벨')
        context["box_label"] = Version.objects.filter(Instrument_Name=Instrument_Nm).filter(SW_Name__contains='박스 라벨')

        return context

    def get_success_url(self):
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])

        # self.Excel_Finished_Inspection1()
        Inspection.objects.filter(Instrument_SN=object_Inspection.Instrument_SN_id).update(Status='검사완료')
        return reverse("Instrumentapp:instrument", kwargs={"category": 'QC', "instrument_name": self.object.Name})


    # 설명 : Seegene STARlet 완제품 성적서 완료시, Excel 데이터 자동 입력 기능
    # 작성자 : 이신후
    # 날짜 : 2022/06/09
    def Excel_Finished_Inspection1(self):
        object_Inspection = get_object_or_404(FinishInspection, Instrument_SN=self.kwargs['Instrument_SN'])
        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Reportfinish.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['1']

        # Inspection
        sheet['K6'] = object_Inspection.Instrument_SN_id # 장비 SN
        sheet['K7'] = object_Inspection.Computer_SN # 컴퓨터 SN
        sheet['K8'] = object_Inspection.Barcode_Scanner # 바코드 스캐너
        sheet['D10'] = object_Inspection.Inspector # 검사자
        sheet['D11'] = self.request.POST.get("CompleteDt") # 완제품 성적서 완료일
        sheet['E16'] = object_Inspection.Completed_Date # 검사완료일
        sheet['D13'] = object_Inspection.SW_Version # SW 버전
        sheet['D14'] = object_Inspection.SL_Version # 씨젠런처 버전

        # sheet['E18'] = object_Inspection.Revision # 검사성적서 Revision
        # sheet['E18'] = object_Inspection.Status # 검사 상태

        # 1. Computer verification
        if object_Inspection.Computer_Version == "Accept":
            sheet['K18'] = "■ Accept          □  Reject "
        elif object_Inspection.Computer_Version == "Reject":
            sheet['K18'] = "□ Accept          ■  Reject "

        # 2. Seegene Launcher Installation process verification
        if object_Inspection.SL_Install == "Accept":
            sheet['K21'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Install == "Reject":
            sheet['K21'] = "□ Accept          ■  Reject "

        if object_Inspection.Method_Import == "Accept":
            sheet['K22'] = "■ Accept          □  Reject "
        elif object_Inspection.Method_Import == "Reject":
            sheet['K22'] = "□ Accept          ■  Reject "

        if object_Inspection.SL_Run_Version == "Accept":
            sheet['K23'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Run_Version == "Reject":
            sheet['K23'] = "□ Accept          ■  Reject "

        # 3. Communication test
        if object_Inspection.SL_Maintenance_Screen == "Accept":
            sheet['K26'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Maintenance_Screen == "Reject":
            sheet['K26'] = "□ Accept          ■  Reject "

        # 4. Seegene Launcher performance verification
        if object_Inspection.SL_Home_Screen == "Accept":
            sheet['K29'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Home_Screen == "Reject":
            sheet['K29'] = "□ Accept          ■  Reject "

        if object_Inspection.SL_mode == "Accept":
            sheet['K30'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_mode == "Reject":
            sheet['K30'] = "□ Accept          ■  Reject "

        if object_Inspection.SL_Protocol == "Accept":
            sheet['K31'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Protocol == "Reject":
            sheet['K31'] = "□ Accept          ■  Reject "

        if object_Inspection.SL_Setting_Screen == "Accept":
            sheet['K32'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Setting_Screen == "Reject":
            sheet['K32'] = "□ Accept          ■  Reject "

        if object_Inspection.SL_Trace == "Accept":
            sheet['K33'] = "■ Accept          □  Reject "
        elif object_Inspection.SL_Trace == "Reject":
            sheet['K33'] = "□ Accept          ■  Reject "

        # 5. Labeling & Packaging inspection
        if object_Inspection.Condition == "Accept":
            sheet['K36'] = "■ Accept          □  Reject "
        elif object_Inspection.Condition == "Reject":
            sheet['Kk36'] = "□ Accept          ■  Reject "

        if object_Inspection.HHS_Labeled == "Accept":
            sheet['K37'] = "■ Accept          □  Reject "
        elif object_Inspection.HHS_Labeled == "Reject":
            sheet['Kk37'] = "□ Accept          ■  Reject "

        if object_Inspection.Acc_Labeled == "Accept":
            sheet['K38'] = "■ Accept          □  Reject "
        elif object_Inspection.Acc_Labeled == "Reject":
            sheet['Kk38'] = "□ Accept          ■  Reject "

        sheet['B39'] = f"[Label] Same as the Labeling & Packaging instruction [      {str(object_Inspection.Labeling_Instruction_Rev)}        ] "
        sheet['B40'] = f"Label No: (Instrument Label) {str(object_Inspection.Labeling_Instruction)}                    (Box Label) {str(object_Inspection.Labeling_Box)}"
        sheet['B41'] = f"S/N :   {str(object_Inspection.Label_SN)}                                            MFG:  {str(object_Inspection.Label_MFG)}"

        if object_Inspection.Label_Option == "Accept":
            sheet['K39'] = "■ Accept          □  Reject "
        elif object_Inspection.Label_Option == "Reject":
            sheet['Kk39'] = "□ Accept          ■  Reject "

        if object_Inspection.UDI_Barcode == "Accept":
            sheet['K42'] = "■ Accept          □  Reject "
        elif object_Inspection.UDI_Barcode == "Reject":
            sheet['Kk42'] = "□ Accept          ■  Reject "

        if object_Inspection.UDI_HRI == "Accept":
            sheet['K43'] = "■ Accept          □  Reject "
        elif object_Inspection.UDI_HRI == "Reject":
            sheet['K43'] = "□ Accept          ■  Reject "

        wb.save('D:\Inst_QC\Reportfinish.xlsx')


