from django.contrib import admin

# Register your models here.
from Manage_Merchant.models import CreateMerchant, PickUp

admin.site.register(CreateMerchant)
admin.site.register(PickUp)
