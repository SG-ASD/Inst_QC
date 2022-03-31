from django.http import HttpResponse

# Create your views here.
from rest_framework.decorators import api_view

from rest_framework.response import Response

# 기존 장고 방식
def hello_world(request):
    return HttpResponse('Hello_world!')

# DRF 방식으로
@api_view()
def hello_world_drf(request):
    return Response({"message": "hello_world!"})

