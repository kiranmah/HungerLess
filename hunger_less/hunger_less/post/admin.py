from django.contrib import admin
from .models import *

class WasteAdmin(admin.ModelAdmin):
    list_display = ('date','address','foodtype','description','quantity','user')
    list_filter = ('date','address','foodtype', 'user')
    search_fields = ['user']
    list_per_page = 50

admin.site.register(post)
admin.site.register(postlink)
admin.site.register(foodtype)
admin.site.register(foodwaste,WasteAdmin)
