from user_profiles.models.Appeal import Appeal
from django.db import models


class EventAppeal(Appeal):
    """
    事件诉求类
    """
    event_name = models.CharField(max_length=255)
