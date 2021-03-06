from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.db import transaction, IntegrityError
from django.http import HttpResponse
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
from AccesorieKitapp.models import Accessories, AccessoriesFiles
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
            sort_CompleteDt = self.request.GET.get("CompleteDt", "")
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
                elif sort_start_date == "????????????":
                    sort_result = instrument_list.order_by("Start_Date")
                elif sort_start_date == "????????????":
                    sort_result = instrument_list.order_by("-Start_Date")
                return sort_result

            if sort_CompleteDt:
                if sort_CompleteDt == "":
                    sort_result = instrument_list
                elif sort_CompleteDt == "????????????":
                    sort_result = instrument_list.order_by("CompleteDt")
                elif sort_CompleteDt == "????????????":
                    sort_result = instrument_list.order_by("-CompleteDt")
                return sort_result

            if sort_inspector:
                if sort_inspector == "":
                    sort_result = instrument_list
                elif sort_inspector == "????????????":
                    sort_result = instrument_list.order_by("Inspector")
                elif sort_inspector == "????????????":
                    sort_result = instrument_list.order_by("-Inspector")
                return sort_result

            if sort_status:
                if sort_status == "":
                    sort_result = instrument_list
                elif sort_status == "????????????":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "???????????????":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "?????????":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "????????????":
                    sort_result = instrument_list.filter(Status=sort_status)
                elif sort_status == "????????????":
                    sort_result = instrument_list.filter(Status=sort_status)
                return sort_result

        return instrument_list

    @transaction.atomic
    def get_context_data(self, **kwargs):
        context = super(InstrumentListView, self).get_context_data(**kwargs)
        instrument_name = self.kwargs.get("instrument_name")
        context["instrument_name"] = instrument_name

        return context

    @transaction.atomic
    def post(self, request, *args, **kwargs):
        instrument_name = self.kwargs.get("instrument_name")
        category = self.kwargs.get("category")

        Start_Date = self.request.POST.get("Start")
        Instrument_SN = request.POST.get('Instrument_SN')

        'D606'
        if self.request.method == "POST":
            # ????????? ??????????????? ?????? ?????? ??????????????? ?????? Try ~ Catch??? ??????
            try:
                excel_data = self.request.POST.get("excel_data")
                inst_SN = self.request.POST.get("s1")

                # ?????? ????????? ?????? ??????
                if excel_data is not None and inst_SN is None:
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
                            Status="????????????",
                            Computer_SN=v[2]
                        )
                        new_Accesories = Accessories.objects.create(
                            Instrument_SN=new_instrument
                        )
                        new_AccessoriesFiles = AccessoriesFiles.objects.create(
                            Instrument_SN=new_instrument
                        )
                        new_FinishInspection = FinishInspection.objects.create(
                            Instrument_SN=new_instrument,
                            Name=v[0],
                            Status="????????????",
                            Computer_SN=v[2]
                        )

                # ?????? ???????????? ?????? ??????
                elif excel_data is None and inst_SN is not None:
                    new_instrument = Instrument.objects.create(
                        SN=inst_SN,
                        Name=instrument_name
                    )
                    new_inspection = Inspection.objects.create(
                        Instrument_SN=new_instrument,
                        Name=instrument_name,
                        Status="????????????"
                    )
                    new_Accesories = Accessories.objects.create(
                        Instrument_SN=new_instrument
                    )
                    new_AccessoriesFiles = AccessoriesFiles.objects.create(
                        Instrument_SN=new_instrument
                    )
                    new_FinishInspection = FinishInspection.objects.create(
                        Instrument_SN=new_instrument,
                        Name=instrument_name,
                        Status="????????????"
                    )
                # ????????? ????????? ????????? ???????????? ?????? IntegrityError??? ??????
                # Html Message tag??? Warning ??????
            except IntegrityError as e:
                print(e)
                messages.warning(request, '????????? ????????? ????????? ????????????. ?????? ??????????????? ???????????? ????????????.')
                return redirect("Instrumentapp:instrument", category, instrument_name)

            if Start_Date is not "" and Instrument_SN is not None:
                Inspection.objects.filter(Instrument_SN=Instrument_SN).update(Start_Date=Start_Date)
                return redirect("Inspectionapp:update", Instrument_SN)

            if excel_data is None and inst_SN is None and Start_Date is "":
                messages.error(request, '???????????? ????????? ???????????????')
                return redirect("Instrumentapp:instrument", category, instrument_name)


            return redirect("Instrumentapp:instrument", category, instrument_name)

        # return render(self.request, "instrument", {'category': category, 'instrument_name': instrument_name})
        return redirect("Instrumentapp:instrument", category, instrument_name)


