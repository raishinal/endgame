from django.contrib import admin
from .models import Games

class GamesAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','platform','publisher','developer','site_link')
    list_display_links= ('id','title',)
    list_filter = ('developer','publisher',)
    search_fields = ('title','publisher','developer','platform','genre',)
    list_per_page = 25
    

admin.site.register(Games,GamesAdmin)
