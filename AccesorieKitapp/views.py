from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView

from Inspectionapp.models import Inspection, Inspection_Category
from .forms import AccList1_UpdateForm, AccList2_UpdateForm, AccList3_UpdateForm
from .models import Accessories
import openpyxl


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
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        context["inspection_subcategory"] = Inspection_Category.objects.filter(Category="Electrical Test").values_list('Subcategory', flat=True)
        return context

    def get_success_url(self):
        object_Inspection = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])

        # 수입검사 성적서 엑셀 파일에 데이터 삽입
        wb = openpyxl.load_workbook('D:\Inst_QC\Report.xlsx', data_only=True)
        sheet = wb.active
        sheet = wb['1']
        sheet['E10'] = object_Inspection.Inspector
        sheet['E11'] = object_Inspection.Start_Date
        sheet['E12'] = object_Inspection.Completed_Date
        sheet['E14'] = object_Inspection.SW_Version
        sheet['E15'] = object_Inspection.FV2_Version
        sheet['E16'] = object_Inspection.FW_PipetteCh
        sheet['E17'] = object_Inspection.FW_Xdrive
        sheet['E18'] = object_Inspection.FW_Master
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
        if object_Inspection .Appearance_Front == "Pass":
            sheet['K33'] = "■ Pass"
            sheet['K34'] = "□  Fail"
        elif object_Inspection.Appearance_Front == "Fail":
            sheet['K33'] = "□  Pass"
            sheet['K34'] = "■  Fail"

        if object_Inspection .Appearance_Top == "Pass":
            sheet['K36'] = "■ Pass"
            sheet['K37'] = "□  Fail"
        elif object_Inspection.Appearance_Top == "Fail":
            sheet['K36'] = "□  Pass"
            sheet['K37'] = "■  Fail"

        if object_Inspection .Appearance_Right == "Pass":
            sheet['K39'] = "■ Pass"
            sheet['K40'] = "□  Fail"
        elif object_Inspection.Appearance_Right == "Fail":
            sheet['K39'] = "□  Pass"
            sheet['K40'] = "■  Fail"

        if object_Inspection .Appearance_Left == "Pass":
            sheet['K42'] = "■ Pass"
            sheet['K43'] = "□  Fail"
        elif object_Inspection.Appearance_Left == "Fail":
            sheet['K42'] = "□  Pass"
            sheet['K43'] = "■  Fail"

        if object_Inspection .Appearance_Back == "Pass":
            sheet['K45'] = "■ Pass"
            sheet['K46'] = "□  Fail"
        elif object_Inspection.Appearance_Back == "Fail":
            sheet['K45'] = "□  Pass"
            sheet['K46'] = "■  Fail"

        # 성적서 2페이지
        sheet = wb.active
        sheet = wb['2']
        sheet['H3'] = "□ No          ■  Yes "
        sheet['H3'] = "□ No          ■  Yes "


        wb.save('D:\Inst_QC\Report.xlsx')

        return reverse("AccesorieKitapp:update_AccKit3", kwargs={"Instrument_SN": self.object.Instrument_SN_id})
