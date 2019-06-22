from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','genre','news_date')
    list_display_links =('id','title')
    search_fields = ('title','genre')
    list_per_page = 25
    


admin.site.register(News, NewsAdmin)
