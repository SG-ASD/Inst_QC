from django.contrib.auth.decorators import login_required
from django.db import transaction
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
from .models import Instrument
from Mainapp.models import Category
from Inspectionapp.models import Inspection
from .forms import InstrumentForm


# Create your views here.


class InstrumentListView(ListView):
    model = Inspection
    template_name = "Instrumentapp/instrument.html"
    context_object_name = "inspection_list"
    pk_url_kwarg = "category"

    # def get_success_url(self):
    #     return reverse('Inspection:update', kwargs={'pk': self.object.pk})

    @transaction.atomic
    def get_queryset(self):
        # instrument_name = self.kwargs.get("instrument_name")
        # instrument_list = Inspection.objects.filter(Name=instrument_name).values().order_by("-id")
        instrument_list = Inspection.objects.values().order_by("-id")

        if self.request.method == "GET":
            search_keyword = self.request.GET.get("q", "")
            sort_name = self.request.GET.get("inst_name", "")
            sort_start_date = self.request.GET.get("start_date", "")
            sort_completed_date = self.request.GET.get("completed_date", "")
            sort_inspector = self.request.GET.get("inspector", "")
            sort_status = self.request.GET.get("status", "")

            if search_keyword:
                search_result = instrument_list.filter(Instrument_SN__SN__icontains=search_keyword)
                print(search_result)
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

        print(f"subcategory : {subcategory}")
        print(f"context : {context}")

        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_name = self.kwargs.get("instrument_name")
        category = self.kwargs.get("category")

        if self.request.method == "POST":
            print(f"self.request.POST : {self.request.POST}")
            inst_name = self.request.POST.get("s1")
            inst_SN = self.request.POST.get("s2")

            context = {"s2": inst_SN, "s1": inst_name}

            # new_inst = Instrument(SN=inst_SN, Name=inst_name)
            # new_inst.save()
            # new_inspection = Inspection(Instrument_SN=new_inst.SN, Name=inst_name, Status="검사대기")
            # new_inspection.save()

            new_instrument = Instrument.objects.create(
                SN=inst_SN,
                Name=inst_name
            )

            new_inspection = Inspection.objects.create(
                Instrument_SN=new_instrument,
                Name=inst_name,
                Status="검사대기"
            )

        print(f"context : {context}")
        print(f"category : {category}")
        print(f"instrument_name : {instrument_name}")

        # return render(self.request, "instrument", {'category': category, 'instrument_name': instrument_name})
        return redirect("Instrumentapp:instrument", category, instrument_name)


# class InstrumentCreateView(CreateView):
#     model = Instrument
#     form_class = InstrumentForm
#     template_name = "Instrumentapp/add_instrument.html"
#     context_object_name = "instrument_list"
#     pk_url_kwarg = "category"
#
#     @transaction.atomic
#     def get_queryset(self):  # ListView가 전달하는 object를 바꾸고 싶으면 get_queryset을 오버라이드 한다.(object 여러개)
#         category = self.kwargs.get("category")
#         temp1 = Category.objects.filter(Category=category).values('Subcategory')
#         # print(Category.objects.filter(Category=main_category).values('Subcategory').query)
#         print(temp1)
#         return temp1
#     def index(self):
#         return render(self.request, "Instrumentapp/add_instrument.html")
#
#     def form_valid(self, form):  # 입력받은 데이터가 유효할 때 데이터로 채워진 모델 오브젝트를 만들고 오브젝트를 저장하는 메소드
#         print("post!!!")
#         print(self.request.POST.get("s1"))
#         # view에서 현재 user에 접근할 때는 request.user를 사용
#         # 저장될 폼에 새로운 속성을 추가하려면 form.instance에 속성을 추가하고 꼭 CreateView의 form_vaild 메소드를 호출해야 한다. 호출하지 않으면 폼이 저장되지 않는다.
#         form.instance.author = self.request.user  # 함수형에서는 request가 view 파라미터로 전달. 클래스형 뷰에서는 self.request로 접근해야 한다.
#         print(f"form.instance : {form.instance}")
#         return super().form_valid(form)  # super는 ReviewCreateView의 상위 클래스, 즉 CreateView를 의미
#
#     def get_success_url(self):
#         category = self.kwargs.get("category")
#         instrument_name = self.kwargs.get("instrument_name")
#         # self.object는 현재 제네릭 뷰가 다루고 있는 object라고 생각하면 된다.
#         return reverse("instrument", kwargs={"category": category, "instrument_name": instrument_name})  # review-detail에 id를 파라미터로 넘긴다.
