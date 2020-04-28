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


@Filters.allow_CDR
def test_for_classify(request):
    if request.method == 'POST':
        appeallor = request.POST.get('iphone_id')
        field_name = request.POST.get('table_name')
    else:
        appeallor = request.GET.get('iphone_id')
        field_name = request.GET.get('table_name')
    print(appeallor, field_name)
    data = {'一级分类': [{'name': '城市建设类', 'value': 914}, {'name': '科教文卫类', 'value': 555}],
            '二级分类': [{'name': '城市建设类', 'value': 329}, {'name': '科教文卫类', 'value': 555}],
            '三级分类': [{'name': '城市建设类', 'value': 666}, {'name': '科教文卫类', 'value': 555}],
            '四级分类': [{'name': '城市建设类', 'value': 222}, {'name': '科教文卫类', 'value': 555}],
            '五级分类': [{'name': '城市建设类', 'value': 333}, {'name': '科教文卫类', 'value': 555}]}
    respond = JsonResponse(data, safe=False)
    return respond


@Filters.allow_CDR
def test_for_upload(request):
    if request.method == 'POST':
        file = request.POST.get('file')
        field_name = request.POST.get('city')
    else:
        file = request.GET.get('file')
        field_name = request.GET.get('city')

    print(file, field_name)
    data = {'一级分类': [{'name': '城市建设类', 'value': 914}, {'name': '科教文卫类', 'value': 555}],
            '二级分类': [{'name': '城市建设类', 'value': 329}, {'name': '科教文卫类', 'value': 555}],
            '三级分类': [{'name': '城市建设类', 'value': 666}, {'name': '科教文卫类', 'value': 555}],
            '四级分类': [{'name': '城市建设类', 'value': 222}, {'name': '科教文卫类', 'value': 555}],
            '五级分类': [{'name': '城市建设类', 'value': 333}, {'name': '科教文卫类', 'value': 555}]}
    respond = JsonResponse(data, safe=False)
    return respond


class StationListView(generics.ListCreateAPIView):
    queryset = PersonalAppeal.objects.all()
    serializer_class = PersonalAppealSerializer
