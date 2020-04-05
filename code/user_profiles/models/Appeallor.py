import mongoengine


class Appeallor(mongoengine.Document):
    """
    诉求人相关信息
    """
    # 姓名
    name = mongoengine.StringField()
    # 是否匿名
    is_anonymous = mongoengine.BooleanField(default=True)
    # 其他信息
    other_info = mongoengine.DictField(default={})
