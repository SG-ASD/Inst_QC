from django.db import transaction
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Category

# Create your views here.


class IndexView(ListView):
    model = Category
    template_name = "Mainapp/index.html"
    context_object_name = "main_category"

    @transaction.atomic
    def get_queryset(self):
        temp1 = Category.objects.distinct().values_list('Category', flat=True)  # distinct() : 중복 제거, values_list() : 특정 필드를 조건으로 지정
        # print(Category.objects.distinct().values_list('Category').query)
        return temp1


class SubcategoryView(ListView):
    model = Category
    template_name = "Mainapp/subcategory.html"
    context_object_name = "sub_category"
    pk_url_kwarg = "category_main"

    @transaction.atomic
    def get_queryset(self):  # ListView가 전달하는 object를 바꾸고 싶으면 get_queryset을 오버라이드 한다.(object 여러개)
        main_category = self.kwargs.get("category_main")
        temp1 = Category.objects.filter(Category=main_category).values()
        # print(Category.objects.filter(Category=main_category).values('Subcategory').query)
        return temp1
