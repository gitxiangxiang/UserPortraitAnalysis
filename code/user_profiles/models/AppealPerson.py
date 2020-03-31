from django.db import models


class AppealPerson(models.Model):
    """
    诉求人
    """
    name = models.CharField(max_length=255)
    profiles = models.TextField()
    anonymous = models.BooleanField(default=True)
