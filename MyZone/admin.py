from django.contrib import admin

# Register your models here.
from MyZone.models import Company, Programmer, Language

admin.site.register(Company)
admin.site.register(Programmer)
admin.site.register(Language)

