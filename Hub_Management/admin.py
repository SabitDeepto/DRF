from django.contrib import admin

# Register your models here.
from Hub_Management.models import CreateHubManager, CreateHub

admin.site.register(CreateHubManager)
admin.site.register(CreateHub)