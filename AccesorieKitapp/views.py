from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from openpyxl.styles import Alignment

from Inspectionapp.models import Inspection, Inspection_Category
from .forms import AccList1_UpdateForm, AccList2_UpdateForm, AccList3_UpdateForm
from .models import Accessories
from Inspectionapp.models import Inspection
import openpyxl


# 설명 : Seegene STARlet 악세서리 키트 첫번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_first(UpdateView):
    model = Accessories
    form_class = AccList1_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_first.html'
    context_object_name = 'target_Acc_first'

    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_first, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit2", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

# 설명 : Seegene STARlet 악세서리 키트 두번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_second(UpdateView):
    model = Accessories
    form_class = AccList2_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_second.html'
    context_object_name = 'target_Acc_second'

    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_second, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        return reverse("AccesorieKitapp:update_AccKit3", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

# 설명 : Seegene STARlet 악세서리 키트 세번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AccKitUpdateView_third(UpdateView):
    model = Accessories
    model_Inspection = Inspection
    form_class = AccList3_UpdateForm
    template_name = 'AccesorieKitapp/AccKitUpdateView_third.html'
    context_object_name = 'target_Acc_third'

    def get_object(self):
        object = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AccKitUpdateView_third, self).get_context_data(**kwargs)
        context["inspection"] = Inspection.objects.filter(Instrument_SN=self.kwargs['Instrument_SN'])
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        CompleteDt= self.request.POST.get("CompleteDt")
        Inspection.objects.filter(Instrument_SN=object_Inspection.Instrument_SN_id).update(CompleteDt=CompleteDt, Status='검사완료')
        # 악세서리 키트에서 완제품 넘어갈 경우, 자동 Excel file 데이터 입력 기능
        self.Excel_Inspection1()
        self.Excel_Inspection2()
        self.Excel_Inspection3()
        self.Excel_Inspection4()


        return reverse("FinishedInspectionapp:update_finish1", kwargs={"Instrument_SN": self.object.Instrument_SN_id})

    def Excel_Inspection1(self):
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Report.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['1']
        sheet['E10'] = object_Inspection.Inspector
        sheet['E11'] = object_Inspection.Start_Date
        sheet['E12'] = object_Inspection.CompleteDt
        sheet['E14'] = object_Inspection.SW_Version
        sheet['E15'] = object_Inspection.FV2_Version
        sheet['E16'] = object_Inspection.FW_PipetteCh
        sheet['E17'] = object_Inspection.FW_Xdrive
        sheet['E18'] = object_Inspection.FW_Master

        sheet['K7'] = object_Inspection.Name
        sheet['K8'] = object_Inspection.Computer_SN

        # Inspection Appearance 부분
        if object_Inspection.Appearance_Shock_Watch == "No":
            sheet['G23'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Shock_Watch == "Yes":
            sheet['G23'] = "□ No          ■  Yes "

        if object_Inspection.Appearance_Binding == "No":
            sheet['G24'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Binding == "Yes":
            sheet['G24'] = "□ No          ■  Yes "

        if object_Inspection.Appearance_Labels == "No":
            sheet['G25'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Labels == "Yes":
            sheet['G25'] = "□ No          ■  Yes "

        if object_Inspection.Appearance_Packaging_Box == "No":
            sheet['G26'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Packaging_Box == "Yes":
            sheet['G26'] = "□ No          ■  Yes "

        if object_Inspection.Appearance_Wooden_Pallet == "No":
            sheet['G27'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Wooden_Pallet == "Yes":
            sheet['G27'] = "□ No          ■  Yes "

        if object_Inspection.Appearance_Transport_Jig == "No":
            sheet['G28'] = "■ No          □  Yes "
        elif object_Inspection.Appearance_Transport_Jig == "Yes":
            sheet['G28'] = "□ No          ■  Yes "

        # Appearance Front / Tip / Right / Left /Back
        if object_Inspection.Appearance_Front == "Pass":
            sheet['K33'] = "■ Pass"
            sheet['K34'] = "□  Fail"
        elif object_Inspection.Appearance_Front == "Fail":
            sheet['K33'] = "□  Pass"
            sheet['K34'] = "■  Fail"

        if object_Inspection.Appearance_Top == "Pass":
            sheet['K36'] = "■ Pass"
            sheet['K37'] = "□  Fail"
        elif object_Inspection.Appearance_Top == "Fail":
            sheet['K36'] = "□  Pass"
            sheet['K37'] = "■  Fail"

        if object_Inspection.Appearance_Right == "Pass":
            sheet['K39'] = "■ Pass"
            sheet['K40'] = "□  Fail"
        elif object_Inspection.Appearance_Right == "Fail":
            sheet['K39'] = "□  Pass"
            sheet['K40'] = "■  Fail"

        if object_Inspection.Appearance_Left == "Pass":
            sheet['K42'] = "■ Pass"
            sheet['K43'] = "□  Fail"
        elif object_Inspection.Appearance_Left == "Fail":
            sheet['K42'] = "□  Pass"
            sheet['K43'] = "■  Fail"

        if object_Inspection.Appearance_Back == "Pass":
            sheet['K45'] = "■ Pass"
            sheet['K46'] = "□  Fail"
        elif object_Inspection.Appearance_Back == "Fail":
            sheet['K45'] = "□  Pass"
            sheet['K46'] = "■  Fail"

        wb.save('D:\Inst_QC\Report.xlsx')



    def Excel_Inspection2(self):
        # 성적서 2페이지
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Report.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['2']
        if object_Inspection.Appearance_Acc_Damage == "Yes":
            sheet['H3'] = "□ No          ■  Yes "
        elif object_Inspection.Appearance_Acc_Damage == "No":
            sheet['H3'] = "■ No          □  Yes "

        if object_Inspection.Appearance_Acc_Missing == "Yes":
            sheet['H4'] = "□ No          ■  Yes "
        elif object_Inspection.Appearance_Acc_Missing == "No":
            sheet['H4'] = "■ No          □  Yes "

        if object_Inspection.ElectricalTest_HiPotential == "Pass":
            sheet['H8'] = "■ Pass          □  Fail"
        elif object_Inspection.ElectricalTest_HiPotential == "Fail":
            sheet['H8'] = "□ Pass          ■  Fail"

        if object_Inspection.ElectricalTest_GroundResistance == "Pass":
            sheet['H9'] = "■ Pass          □  Fail"
        elif object_Inspection.ElectricalTest_GroundResistance == "Fail":
            sheet['H9'] = "□ Pass          ■  Fail"

        if object_Inspection.ElectricalTest_PowerSWFunction == "Pass":
            sheet['H10'] = "■ Pass          □  Fail"
        elif object_Inspection.ElectricalTest_PowerSWFunction == "Fail":
            sheet['H10'] = "□ Pass          ■  Fail"

        if object_Inspection.ElectricalTest_PowerLED == "Pass":
            sheet['H11'] = "■ Pass          □  Fail"
        elif object_Inspection.ElectricalTest_PowerLED == "Fail":
            sheet['H11'] = "□ Pass          ■  Fail"

        sheet['B14'] = "Used Channel Calibration Tool Management No : " + str(
            object_Inspection.HardWare_CalibrationTool)
        sheet['B15'] = "Used Barcode Carrier Management No : " + str(object_Inspection.HardWare_BarcodeCarrier)

        sheet[
            'H17'] = f"     Left :      {object_Inspection.HardWare_XArm_left}               Right :     {object_Inspection.HardWare_XArm_right}       "

        sheet['H18'] = object_Inspection.HardWare_XArm_Diff

        sheet['I20'] = f"X :     {object_Inspection.HardWare_Xdev1}   //  {object_Inspection.HardWare_Xtilt1}"
        sheet['I21'] = f"X :     {object_Inspection.HardWare_Xdev2}   //  {object_Inspection.HardWare_Xtilt2}"
        sheet['I22'] = f"X :     {object_Inspection.HardWare_Xdev3}   //  {object_Inspection.HardWare_Xtilt3}"
        sheet['I23'] = f"X :     {object_Inspection.HardWare_Xdev4}   //  {object_Inspection.HardWare_Xtilt4}"
        sheet['I24'] = f"X :     {object_Inspection.HardWare_Xdev5}   //  {object_Inspection.HardWare_Xtilt5}"
        sheet['I25'] = f"X :     {object_Inspection.HardWare_Xdev6}   //  {object_Inspection.HardWare_Xtilt6}"
        sheet['I26'] = f"X :     {object_Inspection.HardWare_Xdev7}   //  {object_Inspection.HardWare_Xtilt7}"
        sheet['I27'] = f"X :     {object_Inspection.HardWare_Xdev8}   //  {object_Inspection.HardWare_Xtilt8}"

        sheet['J20'] = f"Y :   {object_Inspection.HardWare_Ytilt1}"
        sheet['J21'] = f"Y :   {object_Inspection.HardWare_Ytilt2}"
        sheet['J22'] = f"Y :   {object_Inspection.HardWare_Ytilt3}"
        sheet['J23'] = f"Y :   {object_Inspection.HardWare_Ytilt4}"
        sheet['J24'] = f"Y :   {object_Inspection.HardWare_Ytilt5}"
        sheet['J25'] = f"Y :   {object_Inspection.HardWare_Ytilt6}"
        sheet['J26'] = f"Y :   {object_Inspection.HardWare_Ytilt7}"
        sheet['J27'] = f"Y :   {object_Inspection.HardWare_Ytilt8}"

        sheet['K20'] = object_Inspection.HardWare_SN1
        sheet['K21'] = object_Inspection.HardWare_SN2
        sheet['K22'] = object_Inspection.HardWare_SN3
        sheet['K23'] = object_Inspection.HardWare_SN4
        sheet['K24'] = object_Inspection.HardWare_SN5
        sheet['K25'] = object_Inspection.HardWare_SN6
        sheet['K26'] = object_Inspection.HardWare_SN7
        sheet['K27'] = object_Inspection.HardWare_SN8

        if object_Inspection.HardWare_Adjust == "Pass":
            sheet['E28'] = "■ Pass          □  Fail"
        elif object_Inspection.HardWare_Adjust == "Fail":
            sheet['E28'] = "□ Pass          ■  Fail"

        sheet[
            'I29'] = f"X :    {object_Inspection.HardWare_PIP_X1}                                Y : {object_Inspection.HardWare_PIP_Y1} "
        sheet[
            'I31'] = f"X :    {object_Inspection.HardWare_PIP_X2}                                Y : {object_Inspection.HardWare_PIP_Y2} "
        sheet[
            'I33'] = f"X :    {object_Inspection.HardWare_PIP_X3}                                Y : {object_Inspection.HardWare_PIP_Y3} "
        sheet[
            'I35'] = f"X :    {object_Inspection.HardWare_PIP_X4}                                Y : {object_Inspection.HardWare_PIP_Y4} "
        sheet[
            'I37'] = f"X :    {object_Inspection.HardWare_PIP_X5}                                Y : {object_Inspection.HardWare_PIP_Y5} "
        sheet[
            'I39'] = f"X :    {object_Inspection.HardWare_PIP_X6}                                Y : {object_Inspection.HardWare_PIP_Y6} "
        sheet[
            'I41'] = f"X :    {object_Inspection.HardWare_PIP_X7}                                Y : {object_Inspection.HardWare_PIP_Y7} "
        sheet[
            'I43'] = f"X :    {object_Inspection.HardWare_PIP_X8}                                Y : {object_Inspection.HardWare_PIP_Y8} "

        sheet['I30'] = f"Z : {object_Inspection.HardWare_PIP_Z1}"
        sheet['I32'] = f"Z : {object_Inspection.HardWare_PIP_Z2}"
        sheet['I34'] = f"Z : {object_Inspection.HardWare_PIP_Z3}"
        sheet['I36'] = f"Z : {object_Inspection.HardWare_PIP_Z4}"
        sheet['I38'] = f"Z : {object_Inspection.HardWare_PIP_Z5}"
        sheet['I40'] = f"Z : {object_Inspection.HardWare_PIP_Z6}"
        sheet['I42'] = f"Z : {object_Inspection.HardWare_PIP_Z7}"
        sheet['I44'] = f"Z : {object_Inspection.HardWare_PIP_Z8}"

        if object_Inspection.HardWare_Autoload == "Pass":
            sheet['E45'] = "■ Pass          □  Fail"
        elif object_Inspection.HardWare_Autoload == "Fail":
            sheet['E45'] = "□ Pass          ■  Fail"

        if object_Inspection.HardWare_Noise == "Pass":
            sheet['E46'] = "■ Pass          □  Fail"
        elif object_Inspection.HardWare_Noise == "Fail":
            sheet['E46'] = "□ Pass          ■  Fail"

        wb.save('D:\Inst_QC\Report.xlsx')

    def Excel_Inspection3(self):
        # 성적서 3페이지
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Report.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['3']

        if object_Inspection.Perfomance_CoverSafety == "Pass":
            sheet['L3'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_CoverSafety == "Fail":
            sheet['L3'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_Barcode == "Pass":
            sheet['L5'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_Barcode == "Fail":
            sheet['L5'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_XYZpositioning == "Pass":
            sheet['L7'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_XYZpositioning == "Fail":
            sheet['L7'] = "□ Pass          ■  Fail"

        sheet.merge_cells('C10:D11')
        sheet.merge_cells('C11:D11')
        sheet['C10'] = object_Inspection.Perfomance_HHS_SN
        sheet["C10"].alignment = Alignment(horizontal="center")




        if object_Inspection.Perfomance_HHS_temperature == "Pass":
            sheet['L8'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_HHS_temperature == "Fail":
            sheet['L8'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_HHS_RPM == "Pass":
            sheet['L11'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_HHS_RPM == "Fail":
            sheet['L11'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_Loading_TipCarrier == "Pass":
            sheet['L12'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_Loading_TipCarrier == "Fail":
            sheet['L12'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_Loading_TubeCarrier == "Pass":
            sheet['L13'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_Loading_TubeCarrier == "Fail":
            sheet['L13'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_Loading_mtpCarrier == "Pass":
            sheet['L14'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_Loading_mtpCarrier == "Fail":
            sheet['L14'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_Loading_4mfxCarrier == "Pass":
            sheet['L15'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_Loading_4mfxCarrier == "Fail":
            sheet['L15'] = "□ Pass          ■  Fail"

        # VFV =====================================================================================
        # P1
        if object_Inspection.Perfomance_VFV_Accuracy300ul1 == "Pass":
            sheet['L16'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul1 == "Fail":
            sheet['L16'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul1 == "Pass":
            sheet['L17'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul1 == "Fail":
            sheet['L17'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul1 == "Pass":
            sheet['L18'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul1 == "Fail":
            sheet['L18'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul1 == "Pass":
            sheet['L19'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul1 == "Fail":
            sheet['L19'] = "□ Pass          ■  Fail"

        # P2
        if object_Inspection.Perfomance_VFV_Accuracy300ul2 == "Pass":
            sheet['L20'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul2 == "Fail":
            sheet['L20'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul2 == "Pass":
            sheet['L21'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul2 == "Fail":
            sheet['L21'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul2 == "Pass":
            sheet['L22'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul2 == "Fail":
            sheet['L22'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul2 == "Pass":
            sheet['L23'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul2 == "Fail":
            sheet['L23'] = "□ Pass          ■  Fail"

        # P3
        if object_Inspection.Perfomance_VFV_Accuracy300ul3 == "Pass":
            sheet['L24'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul3 == "Fail":
            sheet['L24'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul3 == "Pass":
            sheet['L25'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul3 == "Fail":
            sheet['L25'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul3 == "Pass":
            sheet['L26'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul3 == "Fail":
            sheet['L26'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul3 == "Pass":
            sheet['L27'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul3 == "Fail":
            sheet['L27'] = "□ Pass          ■  Fail"

        # P4
        if object_Inspection.Perfomance_VFV_Accuracy300ul4 == "Pass":
            sheet['L28'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul4 == "Fail":
            sheet['L28'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul4 == "Pass":
            sheet['L29'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul4 == "Fail":
            sheet['L29'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul4 == "Pass":
            sheet['L30'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul4 == "Fail":
            sheet['L30'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul4 == "Pass":
            sheet['L31'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul4 == "Fail":
            sheet['L31'] = "□ Pass          ■  Fail"

        # P5
        if object_Inspection.Perfomance_VFV_Accuracy300ul5 == "Pass":
            sheet['L32'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul5 == "Fail":
            sheet['L32'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul5 == "Pass":
            sheet['L33'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul5 == "Fail":
            sheet['L33'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul5 == "Pass":
            sheet['L34'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul5 == "Fail":
            sheet['L34'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul5 == "Pass":
            sheet['L35'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul5 == "Fail":
            sheet['L35'] = "□ Pass          ■  Fail"

        # P5
        if object_Inspection.Perfomance_VFV_Accuracy300ul5 == "Pass":
            sheet['L32'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul5 == "Fail":
            sheet['L32'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul5 == "Pass":
            sheet['L33'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul5 == "Fail":
            sheet['L33'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul5 == "Pass":
            sheet['L34'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul5 == "Fail":
            sheet['L34'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul5 == "Pass":
            sheet['L35'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul5 == "Fail":
            sheet['L35'] = "□ Pass          ■  Fail"

        # P6
        if object_Inspection.Perfomance_VFV_Accuracy300ul6 == "Pass":
            sheet['L36'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul6 == "Fail":
            sheet['L36'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul6 == "Pass":
            sheet['L37'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul6 == "Fail":
            sheet['L37'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul6 == "Pass":
            sheet['L38'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul6 == "Fail":
            sheet['L38'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul6 == "Pass":
            sheet['L39'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul6 == "Fail":
            sheet['L39'] = "□ Pass          ■  Fail"

        # P7
        if object_Inspection.Perfomance_VFV_Accuracy300ul7 == "Pass":
            sheet['L40'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul7 == "Fail":
            sheet['L40'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul7 == "Pass":
            sheet['L41'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul7 == "Fail":
            sheet['L41'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul7 == "Pass":
            sheet['L42'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul7 == "Fail":
            sheet['L42'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul7 == "Pass":
            sheet['L43'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul7 == "Fail":
            sheet['L43'] = "□ Pass          ■  Fail"

        # P8
        if object_Inspection.Perfomance_VFV_Accuracy300ul8 == "Pass":
            sheet['L44'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy300ul8 == "Fail":
            sheet['L44'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision300ul8 == "Pass":
            sheet['L45'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision300ul8 == "Fail":
            sheet['L45'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Accuracy1000ul8 == "Pass":
            sheet['L46'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Accuracy1000ul8 == "Fail":
            sheet['L46'] = "□ Pass          ■  Fail"

        if object_Inspection.Perfomance_VFV_Precision1000ul8 == "Pass":
            sheet['L47'] = "■ Pass          □  Fail"
        elif object_Inspection.Perfomance_VFV_Precision1000ul8 == "Fail":
            sheet['L47'] = "□ Pass          ■  Fail"

        # Attachment
        if object_Inspection.Attachment_CoverSafety_Report == "Attached":
            sheet['L51'] = "■"
        if object_Inspection.Attachment_Barcode_Report == "Attached":
            sheet['L52'] = "■"
        if object_Inspection.Attachment_Position_Report == "Attached":
            sheet['L53'] = "■"
        if object_Inspection.Attachment_Declaration_HHS == "Attached":
            sheet['L54'] = "■"
        if object_Inspection.Attachment_Declaration == "Attached":
            sheet['L55'] = "■"
        if object_Inspection.Attachment_Measurement_Protocol == "Attached":
            sheet['L56'] = "■"
        if object_Inspection.Attachment_ElectricalSafety_Report == "Attached":
            sheet['L57'] = "■"

        wb.save('D:\Inst_QC\Report.xlsx')

    def Excel_Inspection4(self):
        # 성적서 2페이지
        object_Accesories = get_object_or_404(Accessories, Instrument_SN=self.kwargs['Instrument_SN'])
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Report.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['4']

        if object_Accesories.Unpack_Instructions == "checked":
            sheet['K7'] = "■"
        if object_Accesories.Installation_Qualification == "checked":
            sheet['K8'] = "■"
        if object_Accesories.Final_Configuation == "checked":
            sheet['K9'] = "■"
        if object_Accesories.Measurement_Protocol == "checked":
            sheet['K10'] = "■"
        if object_Accesories.EU_Declaration == "checked":
            sheet['K11'] = "■"
        if object_Accesories.DeclarationSTARlet == "checked":
            sheet['K12'] = "■"
        if object_Accesories.Declaration_Quality == "checked":
            sheet['K13'] = "■"
        if object_Accesories.Packing_Checklist == "checked":
            sheet['K14'] = "■"
        if object_Accesories.Maintenance == "checked":
            sheet['K15'] = "■"
        if object_Accesories.Channel_Adjust == "checked":
            sheet['K16'] = "■"
        if object_Accesories.Test_Report == "checked":
            sheet['K17'] = "■"
        if object_Accesories.Loading_Table == "checked":
            sheet['K18'] = "■"
        if object_Accesories.Side_Cover_right == "checked":
            sheet['K19'] = "■"
        if object_Accesories.Side_Cover_left == "checked":
            sheet['K20'] = "■"
        if object_Accesories.Rear_Piexiglas == "checked":
            sheet['K21'] = "■"
        if object_Accesories.Top_Plexiglas == "checked":
            sheet['K22'] = "■"
        if object_Accesories.Left_Plexiglas == "checked":
            sheet['K23'] = "■"
        if object_Accesories.Right_Plexiglas == "checked":
            sheet['K24'] = "■"

        # ACC Kit2
        if object_Accesories.Sensor_4L == "checked":
            sheet['K26'] = "■"
        if object_Accesories.Solid_Waste == "checked":
            sheet['K27'] = "■"
        if object_Accesories.USB_Liquid == "checked":
            sheet['K28'] = "■"
        if object_Accesories.USB_Solid_Liquid == "checked":
            sheet['K29'] = "■"
        if object_Accesories.USB_Venus == "checked":
            sheet['K30'] = "■"
        if object_Accesories.Eppendorf == "checked":
            sheet['K31'] = "■"
        if object_Accesories.Core_Gripper == "checked":
            sheet['K32'] = "■"

            sheet['D33'] = f"Teaching Needle(8ea)  [LOT:       {object_Accesories.Needle_Lot}               ]"

        if object_Accesories.Needle_Check == "checked":
            sheet['K33'] = "■"
        if object_Accesories.Separator == "checked":
            sheet['K34'] = "■"
        if object_Accesories.Tip_Eject == "checked":
            sheet['K35'] = "■"
        if object_Accesories.Power_Cord7 == "checked":
            sheet['K36'] = "■"
        if object_Accesories.Power_CordP == "checked":
            sheet['K37'] = "■"
        if object_Accesories.Cable_USB == "checked":
            sheet['K38'] = "■"
        if object_Accesories.Fuse == "checked":
            sheet['K39'] = "■"
        if object_Accesories.Screw == "checked":
            sheet['K40'] = "■"
        if object_Accesories.Fitting == "checked":
            sheet['K41'] = "■"
        if object_Accesories.Liq_Waste == "checked":
            sheet['K42'] = "■"

        # ACC Kit3
        if object_Accesories.XArm == "checked":
            sheet['K44'] = "■"
        if object_Accesories.Bar_Left == "checked":
            sheet['K45'] = "■"
        if object_Accesories.Bar_Top == "checked":
            sheet['K46'] = "■"

        if object_Accesories.Bag == "checked":
            sheet['K48'] = "■"
        if object_Accesories.Tube_32 == "checked":
            sheet['K49'] = "■"
        if object_Accesories.TipRack_5 == "checked":
            sheet['K50'] = "■"
        if object_Accesories.MFX4 == "checked":
            sheet['K51'] = "■"
        if object_Accesories.SEEG == "checked":
            sheet['K52'] = "■"
        if object_Accesories.FLHX == "checked":
            sheet['K53'] = "■"
        if object_Accesories.SOHX == "checked":
            sheet['K54'] = "■"
        if object_Accesories.HHS_Plate == "checked":
            sheet['K55'] = "■"
        if object_Accesories.MTP == "checked":
            sheet['K56'] = "■"
        if object_Accesories.Verify_Kit == "checked":
            sheet['K57'] = "■"
        if object_Accesories.STD == "checked":
            sheet['K58'] = "■"
        if object_Accesories.High == "checked":
            sheet['K59'] = "■"

        sheet['D60'] = f"Hamiltion Heater & Shaker (HHS)   [SN :         {object_Accesories.HHS_SN}               ]"

        if object_Accesories.HHS_Check == "checked":
            sheet['K60'] = "■"
        if object_Accesories.HHS_Manual == "checked":
            sheet['K61'] = "■"
        if object_Accesories.Stop_Barcode == "checked":
            sheet['K62'] = "■"

        sheet['J4'] = object_Inspection.Computer_SN


        wb.save('D:\Inst_QC\Report.xlsx')