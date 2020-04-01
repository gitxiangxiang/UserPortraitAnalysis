from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Appeal(models.Model):
    """
    抽象诉求类，包含诉求的公共属性
    """

    class UrgentLevel(models.IntegerChoices):
        """ 紧急情况枚举类 """
        EMERGENCY = 0, _('EMERGENCY')
        COMMON = 1, _('COMMON')
        INSIGNIFICANT = 2, _('INSIGNIFICANT')
        __empty__ = _('(OTHERS)')

    class RaiseCategory(models.IntegerChoices):
        """来电类别枚举类"""
        CONSULT = 0
        SEEK_HELP = 1
        COMPLAIN = 2
        __empty__ = _('(OTHERS)')

    class RaiseChannel(models.IntegerChoices):
        """受理渠道枚举类"""
        CALL = 0, _('CALL')
        __empty__ = _('(OTHERS)')

    class OrderStatus(models.IntegerChoices):
        """ 工单状态枚举类 """
        FINISH = 0
        TRANSFER = 1
        APARTMENT = 2
        __empty__ = _('(OTHERS)')

    class ReceiveCategory(models.IntegerChoices):
        """ 受理类型枚举类 """
        DIRECT_HANDLE = 0
        TRANSFER_HANDLE = 1
        __empty__ = _('(OTHERS)')

    # 工单编号
    order_no = models.BigIntegerField(unique=True)
    # 受理员工号
    acceptor_no = models.IntegerField(null=True)
    # 受理员
    acceptor_name = models.CharField(max_length=255, null=True)
    # 来电人
    raise_name = models.CharField(max_length=255, default='匿名')
    # 分类
    classification = models.TextField(default='[]')
    # 紧急程度
    urgent_level = models.IntegerField(choices=UrgentLevel.choices, default=1)
    # 来电类别
    raise_category = models.IntegerField(choices=RaiseCategory.choices, default=0)
    # 受理渠道
    raise_channel = models.IntegerField(choices=RaiseChannel.choices, default=0)
    # 主要内容
    content = models.TextField(default='')
    # 受理时间
    raise_time = models.DateTimeField(default='2020-1-1 00:00:00')
    # 受理备注
    notes = models.TextField(default='')
    # 工单状态
    status = models.IntegerField(choices=OrderStatus.choices, default=2)
    # 受理类型
    receive_category = models.IntegerField(choices=ReceiveCategory.choices, default=0)
    # 是否保密
    is_secrecy = models.BooleanField(default=True)
    # 是否回复
    is_reply = models.BooleanField(default=False)
    # 办理单位
    handle_department = models.CharField(max_length=255, default='')
    # 转办时间
    transfer_time = models.DateTimeField(default='2020-1-1 00:00:00')
    # 转办人姓名
    transfer_name = models.CharField(max_length=255, default='')
    # 转办人工号
    transfer_no = models.IntegerField(null=True)
    # 转办意见
    transfer_opinion = models.TextField(default='')
    # 办结时间
    finish_time = models.DateTimeField(default='2020-1-1 00:00:00')
    # 上传时间
    upload_time = models.DateTimeField(auto_now_add=True)

    class Mate(object):
        abstract = True
        app_label = 'user_profiles'

    def __str__(self):
        return self.classification

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


# 以下为测试代码
if __name__ == '__main__':
    pass
