from django.contrib import admin

# Register your models here.
from languages.models import Language, Type, Programmer

admin.site.register(Language)
admin.site.register(Type)
admin.site.register(Programmer)
