from django.db import models
import mongoengine


class PersonalAppeal(mongoengine.Document):
    """
    个人诉求类
    """
    # 工单编号
    order_no = mongoengine.StringField()
    # 受理员工号
    acceptor_no = mongoengine.StringField()
    # 受理员
    acceptor_name = mongoengine.StringField()
    # 来电人
    raise_name = mongoengine.StringField()
    # 分类
    classification = mongoengine.StringField()
    # 紧急程度
    urgent_level = mongoengine.StringField()
    # 来电类别
    raise_category = mongoengine.StringField()
    # 受理渠道
    raise_channel = mongoengine.StringField()
    # 主要内容
    content = mongoengine.StringField()
    # 受理时间
    raise_time = mongoengine.StringField()
    # 受理备注
    notes = mongoengine.StringField()
    # 工单状态
    status = mongoengine.StringField()
    # 受理类型
    receive_category = mongoengine.StringField()
    # 是否保密
    is_secrecy = mongoengine.StringField()
    # 是否回复
    is_reply = mongoengine.StringField()
    # 办理单位
    handle_department = mongoengine.StringField()
    # 转办时间
    transfer_time = mongoengine.StringField()
    # 转办人姓名
    transfer_name = mongoengine.StringField()
    # 转办人工号
    transfer_no = mongoengine.StringField()
    # 转办意见
    transfer_opinion = mongoengine.StringField()
    # 办结时间
    finish_time = mongoengine.StringField()
    # 上传时间
    upload_time = mongoengine.StringField()
