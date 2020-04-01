from user_profiles.models.PersonalAppeal import PersonalAppeal
from user_profiles.models.Appeal_Abandoned import Appeal
from python.readdata import read
from user_profiles.util.AdapterForReadingExcel import AdapterForReadingExcel


class PersonalAppealDao:

    @staticmethod
    def upload_personal_appeal(book_name, sheet_name):
        table = read.read_data_from_excel(book_name, sheet_name)
        table_head = table[0]
        table_body = table[1:]
        records = []
        dic_list = AdapterForReadingExcel.convert(table_head=table_head, records=table_body)
        # [records.append(PersonalAppeal(**dic)) for dic in dic_list]
        for dic in dic_list:
            # try:
                PersonalAppeal(**dic).save()
                # records.append(PersonalAppeal(**dic))
            # except:
            #     pass

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


