from django.contrib import admin

# Register your models here.
from Merchant_Management.models import CreateMerchant, PickUp

admin.site.register(CreateMerchant)
admin.site.register(PickUp)