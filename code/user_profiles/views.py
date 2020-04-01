from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models.PersonalAppeal import PersonalAppeal
from rest_framework_mongoengine import generics
from .models.Serializers import PersonalAppealSerializer
import json
from .dao import PersonalAppealDao
# 本应用视图的公共前缀
view_prefix = ""


def index(request):
    return render(request, view_prefix+"index.html")


def charts(request):
    return render(request, view_prefix+"pages/charts/chartjs.html")


def crud_mongo_test(request):
    PersonalAppealDao.PersonalAppealDao.upload_personal_appeal(r'D:\program\python\PyCharm\UserPortraitAnalysis\数据\个人诉求.xlsx', '第五人')
    pas = PersonalAppeal.objects.all()
    return HttpResponse('上传成功')


class StationListView(generics.ListCreateAPIView):

    queryset = PersonalAppeal.objects.all()
    serializer_class = PersonalAppealSerializer




