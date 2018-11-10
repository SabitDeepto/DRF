from django.contrib import admin

# Register your models here.
from api_test.models import Paradigm, Language, Programmer

admin.site.register(Paradigm)
admin.site.register(Language)
admin.site.register(Programmer)
