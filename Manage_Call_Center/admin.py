from django.contrib import admin

# Register your models here.
from Manage_Call_Center.models import CreateExecutive, UserProfile, HandleRequest

admin.site.register(CreateExecutive)
admin.site.register(UserProfile)
admin.site.register(HandleRequest)
