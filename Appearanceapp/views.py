from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.utils.decorators import method_decorator
from django.views.generic import UpdateView
from Inspectionapp.models import Inspection, Inspection_Category
from Instrumentapp.models import Revision
from Nonconformanceapp.models import Nonconformance
from Userapp.decorators import User_ownership_required
from .forms import AppearanceUpdateForm, AppearanceUnpackingForm
from QC_util import Util
from datetime import datetime
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

            if request.POST.get('Nonconformance'):
                print("부적합 검사입니다.")
                inspection = Inspection.objects.get(pk=instrument_SN)
                now = datetime.now()
                new_nonconformance = Nonconformance.objects.create(
                    Instrument_SN=inspection.Instrument_SN,
                    Computer_SN=inspection.Computer_SN,
                    Name=inspection.Name,
                    Inspector=inspection.Inspector,
                    Start_Date=now.strftime('%Y-%m-%d'),
                    Doc_Num="QFI-0804-NSS-01",
                    Revision="0",
                    Issue_Num="QFI-0804B-" + f"{inspection.Instrument_SN}",
                    Category="Packaging Condition",
                )

                return redirect('Nonconformanceapp:update', instrument_SN)

            elif form.is_valid():  # 폼이 유효하면
                # db에 값 저장
                form_instance = get_object_or_404(Inspection, Instrument_SN=instrument_SN)  # 현재 Inspection 인스턴스를 불러온다.

                if request.POST.get('Appearance_Shock_Watch') is None:
                    temp1 = ""
                else:
                    temp1 = request.POST.get('Appearance_Shock_Watch')
                if request.POST.get('Appearance_Binding') is None:
                    temp2 = ""
                else:
                    temp2 = request.POST.get('Appearance_Binding')
                if request.POST.get('Appearance_Labels') is None:
                    temp3 = ""
                else:
                    temp3 = request.POST.get('Appearance_Labels')
                if request.POST.get('Appearance_Packaging_Box') is None:
                    temp4 = ""
                else:
                    temp4 = request.POST.get('Appearance_Packaging_Box')
                if request.POST.get('Appearance_Wooden_Pallet') is None:
                    temp5 = ""
                else:
                    temp5 = request.POST.get('Appearance_Wooden_Pallet')
                if request.POST.get('Appearance_Transport_Jig') is None:
                    temp6 = ""
                else:
                    temp6 = request.POST.get('Appearance_Transport_Jig')
                form_instance.Appearance_Shock_Watch = temp1
                form_instance.Appearance_Binding = temp2
                form_instance.Appearance_Labels = temp3
                form_instance.Appearance_Packaging_Box = temp4
                form_instance.Appearance_Wooden_Pallet = temp5
                form_instance.Appearance_Transport_Jig = temp6

                # 파일 upload
                NAS_path = r"\home\windows\품질관리_장비inspection\01 검사 성적서 관리\2022 검사 성적서\QC SW 테스트"  # NAS 폴더 경로
                path = NAS_path + '\\' + instrument_SN
                path = path.replace('\\', '/')

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
