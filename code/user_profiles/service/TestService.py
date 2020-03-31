from ..dao import PersonalAppealDao
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


class TestPersonalAppealDao:
    """
    用于写测试方法
    """
    @staticmethod
    def test_gdocf(request, field_name):
        """
        测试URL模式是否生效
        :param request:
        :param field_name: 
        :return:
        """
        print(PersonalAppealDao.PersonalAppealDao.get_dist_cert_field(field_name))
        return HttpResponse(PersonalAppealDao.PersonalAppealDao.get_dist_cert_field(field_name).__str__())

    @staticmethod
    def test_gdocf2(request):
        """
        测试是否成功从request中取得参数
        :param request:
        :return:
        """
        if request.method == 'POST':
            field_name = request.POST.get('field')
        else:
            field_name = request.GET.get('field')
        print(PersonalAppealDao.PersonalAppealDao.get_dist_cert_field(field_name))
        return HttpResponse(PersonalAppealDao.PersonalAppealDao.get_dist_cert_field(field_name).__str__())