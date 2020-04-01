import mongoengine
from . import Appeal


class PersonalAppeal(Appeal.Appeal):
    """
    个人诉求类
    """

    # 诉求类型
    appeal_type = mongoengine.StringField(default='个人诉求')
