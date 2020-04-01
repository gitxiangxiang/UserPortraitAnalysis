from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user_profiles.models.PersonalAppeal import PersonalAppeal
from rest_framework_mongoengine import generics
from user_profiles.models.Serializers import PersonalAppealSerializer
from ..service import PersistentService
import json


def index(request):
    return render(request, "index.html")


def charts(request):
    return render(request, "pages/charts/chartjs.html")


def save_excel(request):
    path = 'D:\\program\\python\\PyCharm\\UserPortraitAnalysis\\数据\\'
    book_name = '个人诉求.xlsx'
    sheet_name = '第五人'
    if PersistentService.persistent_excel(path, book_name, sheet_name):
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')



class StationListView(generics.ListCreateAPIView):

    queryset = PersonalAppeal.objects.all()
    serializer_class = PersonalAppealSerializer




