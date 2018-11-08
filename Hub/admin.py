from django.contrib import admin

# Register your models here.
from Hub.models import HubManager

admin.site.register(HubManager)

admin.site.site_header = 'TikTok BackEnd'
