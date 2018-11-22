
from django.contrib import admin

# Register your models here.
from Manage_Merchants.models import CreateMerchant, PickUp

admin.site.register(CreateMerchant)


class PickUpAdmin(admin.ModelAdmin):
    list_display = ('action', 'merchant_name', 'address', 'contact_number', )


admin.site.register(PickUp, PickUpAdmin)

