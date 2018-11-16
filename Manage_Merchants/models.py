from django.db import models


# admin can register merchant
class CreateMerchant(models.Model):
    merchant_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)

    def __str__(self):
        return self.merchant_name


# Pick up request from merchant to hub
class PickUp(models.Model):
    merchant_name = models.ForeignKey(CreateMerchant, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    product_details = models.TextField()
    product_quantity = models.IntegerField()
    contact_number = models.CharField(max_length=100)

    COLOR_CHOICES = (
        ('Queue', 'Just Save'),
        ('Pickup Request', 'Request for Pickup'),

    )

    action = models.CharField(max_length=100, choices=COLOR_CHOICES, default='Queue')

    def __str__(self):
        return self.action
