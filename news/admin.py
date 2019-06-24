from django.contrib import admin
from .models import News

class NewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','news_date','is_trending',)
    list_display_links =('id','title')
    search_fields = ('title',)
    list_editable = ('is_trending',)
    list_per_page = 25
    


admin.site.register(News, NewsAdmin)
