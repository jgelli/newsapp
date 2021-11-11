from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.

class ListAds(admin.ModelAdmin):
    list_display = ('id', 'name',)
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_per_page = 10

admin.site.register(Advertising, ListAds)
