from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from user_profiles.models.PersonalAppeal import PersonalAppeal
from rest_framework_mongoengine import generics
from user_profiles.models.Serializers import PersonalAppealSerializer
from ..service import PersistentService
from user_profiles import settings
import os
from user_profiles.util.filters import Filters
import json


def index(request):
    return render(request, "index.html")


def charts(request):
    return render(request, "pages/charts/chartjs.html")


def save_excel(request):
    path = os.path.join(settings.BASE_DIR, 'excel', '')
    book_name = '个人诉求.xlsx'
    sheet_name = '第五人'
    if PersistentService.persistent_excel(path, book_name, sheet_name):
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')


@Filters.allow_CDR
def test_for_front(requset):
    data = {}
    dimensions = ['工单状态', '数量', '数量2']
    source = [{'工单状态': '办结', '数量': 2720, '数量2': 200}
        , {'工单状态': '已转办待回复', '数量': 114, '数量2': 200}
        , {'工单状态': '部门回复', '数量': 32, '数量2': 200}
        , {'工单状态': '部门回退', '数量': 2, '数量2': 200}]
    data['dimensions'] = dimensions
    data['source'] = source
    respond = JsonResponse(data, safe=False)
    return respond


class StationListView(generics.ListCreateAPIView):
    queryset = PersonalAppeal.objects.all()
    serializer_class = PersonalAppealSerializer
