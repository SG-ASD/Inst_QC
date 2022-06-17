from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_protect
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from FinishedInspectionapp.models import FinishInspection
from .models import Instrument
from Mainapp.models import Category
from Inspectionapp.models import Inspection
from AccesorieKitapp.models import Accessories
from .forms import InstrumentForm


# Create your views here.


class InstrumentListView(ListView):
    model = Inspection
    template_name = "Instrumentapp/instrument.html"
    context_object_name = "inspection_list"
    pk_url_kwarg = "category"

    @transaction.atomic
    def get_queryset(self):
        instrument_name = self.kwargs.get("instrument_name")
        instrument_list = Inspection.objects.filter(Name=instrument_name).values()
        # instrument_list = Inspection.objects.values().order_by("-id")
        # instrument_list = Inspection.objects.values()

        if self.request.method == "GET":
            search_keyword = self.request.GET.get("q", "")
            sort_name = self.request.GET.get("inst_name", "")
            sort_start_date = self.request.GET.get("start_date", "")
            sort_completed_date = self.request.GET.get("completed_date", "")
            sort_inspector = self.request.GET.get("inspector", "")
            sort_status = self.request.GET.get("status", "")

            if search_keyword:
                search_result = instrument_list.filter(Instrument_SN__SN__icontains=search_keyword)
                return search_result

            if sort_name:
                if sort_name == "":
                    sort_result = instrument_list
                else:
                    sort_result = instrument_list.filter(Name=sort_name)
                return sort_result

            if sort_start_date:
                if sort_start_date == "":
                    sort_result = instrument_list
                elif sort_start_date == "오름차순":
                    sort_result = instrument_list.order_by("Start_Date")
                elif sort_start_date == "내림차순":
                    sort_result = instrument_list.order_by("-Start_Date")
                return sort_result

            if sort_completed_date:
                if sort_completed_date == "":
                    sort_result = instrument_list
                elif sort_completed_date == "오름차순":
                    sort_result = instrument_list.order_by("Completed_Date")
                elif sort_completed_date == "내림차순":
                    sort_result = instrument_list.order_by("-Completed_Date")
                return sort_result

            if sort_inspector:
                if sort_inspector == "":
                    sort_result = instrument_list
                elif sort_inspector == "오름차순":
                    sort_result = instrument_list.order_by("Inspector")
                elif sort_inspector == "내림차순":
                    sort_result = instrument_list.order_by("-Inspector")
                return sort_result

            if sort_status:
                if sort_status == "":
                    sort_result = instrument_list
                elif sort_status == "검사대기":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "검사진행중":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "부적합":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "재검사중":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "검사완료":
                    sort_result = instrument_list.filter(Status=sort_status)
                return sort_result

        return instrument_list

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(InstrumentListView, self).get_context_data(**kwargs)
        subcategory = self.kwargs.get("category")
        context["subcategory_list"] = Category.objects.filter(Category=subcategory).values()

        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_name = self.kwargs.get("instrument_name")
        category = self.kwargs.get("category")

        if self.request.method == "POST":
            # 동일한 시리얼번호 장비 추가 예외처리를 위한 Try ~ Catch문 사용
            try:
                excel_data = self.request.POST.get("excel_data")
                inst_name = self.request.POST.get("s1")
                inst_SN = self.request.POST.get("s2")

                # 엑셀 파일로 장비 추가
                if excel_data is not None and (inst_name is None or inst_SN is None):
                    excel_data = excel_data.split(',')
                    list_data = []
                    n = -1
                    for idx, v in enumerate(excel_data):
                        if idx % 3 == 0:
                            list_data.append([])
                            n += 1
                        list_data[n].append(v)
                    del list_data[0]

                    for idx, v in enumerate(list_data):
                        new_instrument = Instrument.objects.create(
                            SN=v[1],
                            Name=v[0]
                        )
                        new_inspection = Inspection.objects.create(
                            Instrument_SN=new_instrument,
                            Name=v[0],
                            Status="검사대기",
                            Computer_SN=v[2]
                        )
                        new_Accesories = Accessories.objects.create(
                            Instrument_SN=new_instrument
                        )
                        new_FinishInspection = FinishInspection.objects.create(
                            Instrument_SN=new_instrument,
                            Name=v[0],
                            Status="검사대기",
                            Computer_SN=v[2]
                        )

                # 직접 입력하여 장비 추가
                elif excel_data is None and inst_name is not None and inst_SN is not None:
                    new_instrument = Instrument.objects.create(
                        SN=inst_SN,
                        Name=inst_name
                    )
                    new_inspection = Inspection.objects.create(
                        Instrument_SN=new_instrument,
                        Name=inst_name,
                        Status="검사대기"
                    )
                    new_Accesories = Accessories.objects.create(
                        Instrument_SN=new_instrument
                    )
                    new_FinishInspection = FinishInspection.objects.create(
                        Instrument_SN=new_instrument,
                        Name=inst_name,
                        Status="검사대기"
                    )
            # 기존에 시리얼 번호가 있을경우 해당 IntegrityError가 발생
            # Html Message tag에 Warning 전달
            except IntegrityError:
                messages.warning(request, '기존에 시리얼 번호가 있습니다. 다시 장비추가를 해주시기 바랍니다.')
                return redirect("Instrumentapp:instrument", category, instrument_name)


            # new_inst = Instrument(SN=inst_SN, Name=inst_name)
            # new_inst.save()
            # new_inspection = Inspection(Instrument_SN=new_inst.SN, Name=inst_name, Status="검사대기")
            # new_inspection.save()

        # return render(self.request, "instrument", {'category': category, 'instrument_name': instrument_name})
        return redirect("Instrumentapp:instrument", category, instrument_name)
