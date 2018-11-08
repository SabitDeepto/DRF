from django.db import models


# Create your models here.
class HubManager(models.Model):
    Notification = "1 pickup request"

    def __str__(self):
        return self.Notification
