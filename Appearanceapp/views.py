from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from Inspectionapp.models import Inspection, Inspection_Category
from Instrumentapp.models import Revision
from Userapp.decorators import User_ownership_required
from .forms import AppearanceUpdateForm, AppearanceUnpackingForm
from QC_util import Util
import os
# Create your views here.

has_ownership = [User_ownership_required]


# 설명 : Seegene STARlet Appearance 업데이트 뷰 첫번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AppearanceUpdateView(UpdateView):
    model = Inspection
    form_class = AppearanceUpdateForm
    template_name = 'Appearanceapp/update.html'
    context_object_name = 'target_Appearance'

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AppearanceUpdateView, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_success_url(self):
        # return reverse('Instrumentapp:instrument', kwargs={'pk': self.object.pk})
        return reverse("Appearanceapp:update_Unpacking", kwargs={"Instrument_SN": self.object})

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_SN = self.kwargs.get('Instrument_SN')

        if request.method == 'POST':
            form = AppearanceUpdateForm(request.POST)  # request된 폼

            if form.is_valid():  # 폼이 유효하면
                # db에 값 저장
                form_instance = get_object_or_404(Inspection, Instrument_SN=instrument_SN)  # 현재 Inspection 인스턴스를 불러온다.
                form_instance.Appearance_Shock_Watch = request.POST.get('Appearance_Shock_Watch')
                form_instance.Appearance_Binding = request.POST.get('Appearance_Binding')
                form_instance.Appearance_Labels = request.POST.get('Appearance_Labels')
                form_instance.Appearance_Packaging_Box = request.POST.get('Appearance_Packaging_Box')
                form_instance.Appearance_Wooden_Pallet = request.POST.get('Appearance_Wooden_Pallet')
                form_instance.Appearance_Transport_Jig = request.POST.get('Appearance_Transport_Jig')

                # 파일 upload
                NAS_path = r'\\10.10.102.76\장비품질관리팀\품질관리_장비inspection\01 검사 성적서 관리\2022 검사 성적서\QC SW 테스트'  # NAS 폴더 경로
                path = NAS_path + '\\' + instrument_SN

                if request.FILES.getlist('Appearance_Shock_Watch_Image'):
                    Shock_Watch_files = request.FILES.getlist('Appearance_Shock_Watch_Image')
                    Shock_Watch_files_name = Util.upload_files(self, Shock_Watch_files, path, 'Shock Watch', True)
                    form_instance.Appearance_Shock_Watch_Image = Shock_Watch_files_name
                else:
                    form_instance.Appearance_Shock_Watch_Image = ""

                if request.FILES.getlist('Appearance_Binding_Image'):
                    Binding_files = request.FILES.getlist('Appearance_Binding_Image')
                    Binding_files_name = Util.upload_files(self, Binding_files, path, 'Binding', True)
                    form_instance.Appearance_Binding_Image = Binding_files_name
                else:
                    form_instance.Appearance_Binding_Image = ""

                if request.FILES.getlist('Appearance_Labels_Image'):
                    Labels_files = request.FILES.getlist('Appearance_Labels_Image')
                    Labels_files_name = Util.upload_files(self, Labels_files, path, 'Labels', True)
                    form_instance.Appearance_Labels_Image = Labels_files_name
                else:
                    form_instance.Appearance_Labels_Image = ""

                if request.FILES.getlist('Appearance_Packaging_Box_Image'):
                    Packaging_Box_files = request.FILES.getlist('Appearance_Packaging_Box_Image')
                    Packaging_Box_files_name = Util.upload_files(self, Packaging_Box_files, path, 'Packaging Box', True)
                    form_instance.Appearance_Packaging_Box_Image = Packaging_Box_files_name
                else:
                    form_instance.Appearance_Packaging_Box_Image = ""

                if request.FILES.getlist('Appearance_Wooden_Pallet_Image'):
                    Wooden_Pallet_files = request.FILES.getlist('Appearance_Wooden_Pallet_Image')
                    Wooden_Pallet_files_name = Util.upload_files(self, Wooden_Pallet_files, path, 'Wooden Pallet', True)
                    form_instance.Appearance_Wooden_Pallet_Image = Wooden_Pallet_files_name
                else:
                    form_instance.Appearance_Wooden_Pallet_Image = ""

                if request.FILES.getlist('Appearance_Transport_Jig_Image'):
                    Transport_Jig_files = request.FILES.getlist('Appearance_Transport_Jig_Image')
                    Transport_Jig_files_name = Util.upload_files(self, Transport_Jig_files, path, 'Transport Jig', True)
                    form_instance.Appearance_Transport_Jig_Image = Transport_Jig_files_name
                else:
                    form_instance.Appearance_Transport_Jig_Image = ""

                if request.FILES.getlist('Appearance_Video'):
                    Appearance_Video_files = request.FILES.getlist('Appearance_Video')
                    Appearance_Video_files_name = Util.upload_files(self, Appearance_Video_files, path, 'Unpacking', True)
                    form_instance.Appearance_Video = Appearance_Video_files_name
                else:
                    form_instance.Appearance_Video = ""

                form_instance.save()

                return redirect('Appearanceapp:update_Unpacking', instrument_SN)
            else:
                return redirect('Appearanceapp:update_Packaging', instrument_SN)


# 설명 : Seegene STARlet Appearance 업데이트 뷰 두번째 화면
# 작성자 : 이신후
# 날짜 : 2022/06/09
@method_decorator(login_required, 'get')
@method_decorator(login_required, 'post')
class AppearanceUnpackingView(UpdateView):
    model = Inspection
    form_class = AppearanceUnpackingForm
    template_name = 'Appearanceapp/Unpacking_State.html'
    context_object_name = 'target_Unpacking_State'

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(AppearanceUnpackingView, self).get_context_data(**kwargs)
        context["inspection_category"] = Inspection_Category.objects.distinct().values_list('Category', flat=True)
        return context

    def get_object(self):
        object = get_object_or_404(Inspection, Instrument_SN=self.kwargs['Instrument_SN'])
        return object

    def get_success_url(self):
        return reverse("Electricalapp:update_Electrical", kwargs={"Instrument_SN": self.object})
