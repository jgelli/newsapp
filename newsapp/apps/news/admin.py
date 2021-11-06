from django.contrib import admin
from django.contrib.admin.decorators import display
from .models import *

# Register your models here.

class ListNews(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'status')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    list_filter = ('topic',)
    list_editable = ('status',)
    list_per_page = 10

admin.site.register(News, ListNews)
admin.site.register(Topic)
