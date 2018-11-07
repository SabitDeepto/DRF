from django.db import models


# Create your models here.
class CreateMerchant(models.Model):
    merchant_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.merchant_name