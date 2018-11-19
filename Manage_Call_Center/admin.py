from django.contrib import admin

# Register your models here.
from Manage_Call_Center.models import CreateExecutive, HandleRequest

admin.site.register(CreateExecutive)
admin.site.register(HandleRequest)
