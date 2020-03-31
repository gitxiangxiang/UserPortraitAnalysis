from django.db import models


class Event(models.Model):
    """
    事件类
    """
    profiles = models.TextField()
