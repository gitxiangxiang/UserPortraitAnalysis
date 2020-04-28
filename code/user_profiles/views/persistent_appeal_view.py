import json
import hashlib
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from user_profiles.service import PersistentService
from user_profiles import settings
from user_profiles.util.filters import Filters
import os


@Filters.allow_CDR
def upload_excel(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        myFile = request.FILES.get("file", None)  # 获取上传的文件，如果没有文件，则默认为None
        # 避免文件名重复
        time_now = timezone.now()  # 获取当前日期时间
        m = hashlib.md5()
        m.update(str(time_now).encode())  # 给当前时间编码
        file_id = m.hexdigest()
        path = os.path.abspath('./user_profiles/excel/')
        destination = open(os.path.join(path, file_id + myFile.name), 'wb+')  # 打开特定的文件进行二进制的写操作

        for chunk in myFile.chunks():  # 分块写入文件
            destination.write(chunk)
        destination.close()
        response = {
            'msg': 'success',
            'file_id': file_id+myFile.name,
        }
        return JsonResponse(response)

@Filters.allow_CDR
def do_persistent(request):
    if request.method == "POST":  # 请求方法为POST时，进行处理
        sheet_name = request.POST['sheet_name']
        file_id = request.POST['file_id']
        path = os.path.abspath('./user_profiles/excel/')
        PersistentService.persistent_excel(os.path.join(path, file_id), sheet_name)
        response = {
            'msg': 'success',
        }
        return JsonResponse(response)


# @Filters.allow_CDR
# def label_gjflH(request):
#     if (request.method == 'POST'):
#         data = {}
#         data["city"] = request.POST["table_name"]
#         data["来电号码"] = request.POST["phone_id"]
#
#         '''取到所有的工单数据，放到all_datas中,若电话号码为无，则是热点事件，若有，则是一个用户'''
#         # if(data["来电号码"] == "无"):
#         #     all_datas = mu.select_all_data(data["city"])
#         # else:
#         #     all_datas = mu.search_condition(data["city"], "来电号码", data["来电号码"])
#         all_datas = []
#         labels = {"一级分类":{},"二级分类":{},"三级分类":{},"四级分类":{},"五级分类":{}}
#         #统计各级分类分布数据
#         for data in all_datas:
#             for key,value in labels.items():
#                 try:
#                     if(data[key] in value):
#                         value[data[key]] += 1
#                     else:
#                         value[data[key]] = 1
#                 except:
#                     continue
#         label = {}
#         #排序，只显示top20
#         for key,value in labels.items():
#             label[key] = {}
#             for k in sorted(value, key=value.__getitem__, reverse=True)[:20]:  # 按照值进行排序，取候选词
#                 if(k != "NULL"):
#                     label[key][k] = value[k]
#         print(label)
#
#         return HttpResponse(
#             json.dumps({"result": label}, ensure_ascii=False))




