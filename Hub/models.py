from django.db import models


# Create your models here.
from Manage_Merchant.models import PickUp


class HubManager(models.Model):
    order = models.CharField(default="#", max_length=120)
    pickup_request = models.ForeignKey(PickUp, on_delete=models.CASCADE)

    def __str__(self):
        return self.order
