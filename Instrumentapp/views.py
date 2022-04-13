from django.db import transaction
from django.shortcuts import render, get_object_or_404
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
from .models import Instrument, Inspection
from Mainapp.models import Category
from .forms import InstrumentForm

# Create your views here.


class Instrument_View(ListView):
    model = Inspection
    form_class = InstrumentForm
    template_name = "Instrumentapp/instrument.html"
    # pk_url_kwarg = "instrument_name"
    context_object_name = "instrument_list"

    # context_object_name_2 = "category_list"
    pk_url_kwarg = "category"

    def form_valid(self, form):  # 입력받은 데이터가 유효할 때 데이터로 채워진 모델 오브젝트를 만들고 오브젝트를 저장하는 메소드
        # 함수형에서는 request가 view 파라미터로 전달. 클래스형 뷰에서는 self.request로 접근해야 한다.
        print("form_valid")
        return super().form_valid(form)  # super는 ReviewCreateView의 상위 클래스, 즉 CreateView를 의미

    def post(self, request, *args, **kwargs):
        instrument_list = Inspection.objects.values().order_by("-id")

        if self.request.method == "POST":
            print(f"self.request.POST : {self.request.POST}")
            inst_name = self.request.POST.get("s1")
            inst_SN = self.request.POST.get("s2")

            context = {"s2": inst_SN, "s1": inst_name}

            new_inst = Instrument(SN=inst_SN, Name=inst_name)
            new_inspection = Inspection(SN=inst_SN, Name=inst_name, Status="검사대기")

            new_inst.save()
            new_inspection.save()

        print(f"context : {context}")

        return render(self.request, "Instrumentapp/instrument.html")

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(Instrument_View, self).get_context_data(**kwargs)
        print("get_context_data")
        subcategory = self.kwargs.get("category")
        context["subcategory_list"] = Category.objects.filter(Category=subcategory).values()

        print(f"subcategory : {subcategory}")
        print(f"context : {context}")

        return context

    @transaction.atomic
    def get_queryset(self):
        print("get_queryset")
        instrument_name = self.kwargs.get("instrument_name")
        # instrument_list = Inspection.objects.filter(Name=instrument_name).values().order_by("-id")
        instrument_list = Inspection.objects.values().order_by("-id")

        if self.request.method == "GET":
            search_keyword = self.request.GET.get("q", "")
            sort_name = self.request.GET.get("inst_name", "")
            sort_start_date = self.request.GET.get("start_date", "")
            sort_completed_date = self.request.GET.get("completed_date", "")
            sort_inspector = self.request.GET.get("inspector", "")
            sort_status = self.request.GET.get("status", "")

            print(f"sort_name : {sort_name}")

            if search_keyword:
                search_result = instrument_list.filter(SN__icontains=search_keyword)
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
