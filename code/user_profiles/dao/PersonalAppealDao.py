from mongoengine import Q

from user_profiles.models.PersonalAppeal import PersonalAppeal
from python.readdata import read
from user_profiles.util.AdapterForReadingExcel import AdapterForReadingExcel
from user_profiles.dao.appeallor_dao import AppeallorDao


class PersonalAppealDao:

    @staticmethod
    def save_personal_appeal(book_name, sheet_name):
        table = read.read_data_from_excel(book_name, sheet_name)
        table_head = table[0]
        table_body = table[1:]
        dic_list = AdapterForReadingExcel.convert(table_head=table_head, records=table_body)
        appeallor_name = dic_list[0].get('raise_name')
        appeallor = AppeallorDao.save_appeallor(appeallor_name)
        for dic in dic_list:
            dic['appeallor_id'] = appeallor.id
            PersonalAppeal(**dic).save()

    @staticmethod
    def get_dist_cert_field(appeallor, field_name):
        appe = AppeallorDao.get_appeallor_by_name(appeallor)
        if appe is None:
            return {}
        personal_appeals = PersonalAppeal.objects(appeallor_id=appe.id)
        field = AdapterForReadingExcel.personal_field[field_name]
        dic_field = {}
        for personal_appeal in personal_appeals:
            if personal_appeal[field] in dic_field.keys():
                dic_field[personal_appeal[field]] += 1
            else:
                dic_field[personal_appeal[field]] = 1
        return dic_field

    @staticmethod
    def get_by_time_range(appeallor, start_time, end_time):
        appe = AppeallorDao.get_appeallor_by_name(appeallor)
        if appe is None:
            return []
        personal_appeal = PersonalAppeal.objects(Q(appeallor_id=appe.id)
                                                 & Q(raise_time__gte=start_time) & Q(
            raise_time__lte=end_time)).order_by('raise_time')
        return personal_appeal
