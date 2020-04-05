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

    # 这个方法暂时还不能用，没有筛选特定诉求人的诉求
    @staticmethod
    def get_dist_cert_field(field_name):
        personal_appeals = PersonalAppeal.objects.all()
        field = AdapterForReadingExcel.personal_field[field_name]
        dic_field = {}
        for personal_appeal in personal_appeals:
            if personal_appeal[field] in dic_field.keys():
                dic_field[personal_appeal[field]] += 1
            else:
                dic_field[personal_appeal[field]] = 1
        return dic_field
