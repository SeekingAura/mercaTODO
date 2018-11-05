from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *
# Register your models here.
class SiteAdmin(ModelAdmin):
    list_display = ('name','address')

admin.site.register(Site, SiteAdmin)
