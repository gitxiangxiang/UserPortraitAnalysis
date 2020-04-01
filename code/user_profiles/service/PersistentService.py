from ..dao.PersonalAppealDao import PersonalAppealDao


def persistent_excel(path, book_name, sheet_name):
    try:
        PersonalAppealDao.upload_personal_appeal(path+book_name, sheet_name)
    except Exception:
        print(Exception.__str__)
        return False
    return True
