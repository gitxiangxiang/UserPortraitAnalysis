from django.http import HttpResponse, JsonResponse
from user_profiles.service import PersistentService
from user_profiles import settings
import os


def upload_excel():
    # 当前有一个问题：要解决Excel的同名问题
    path = os.path.join(settings.BASE_DIR, 'excel', '')
    book_name = '个人诉求.xlsx'
    sheet_name = '第五人'
    if PersistentService.persistent_excel(path, book_name, sheet_name):
        return HttpResponse('上传成功')
    else:
        return HttpResponse('上传失败')



