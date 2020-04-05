from ..dao.PersonalAppealDao import PersonalAppealDao


def persistent_excel(path, book_name, sheet_name):
    # try:
    PersonalAppealDao.save_personal_appeal(path+book_name, sheet_name)
    # except Exception:
    #     print(Exception)
    #     return False
    return True
