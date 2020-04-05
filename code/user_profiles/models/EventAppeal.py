import mongoengine
from . import Appeal


class EventAppeal(Appeal.Appeal):
    """
    事件诉求类
    """

    # 诉求类型
    appeal_type = mongoengine.StringField(default='事件诉求')
    # 事件名称
    event_name = mongoengine.StringField()
