from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','rating','date','game','is_trending')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_editable = ('rating','is_trending',)


admin.site.register(Reviews,ReviewsAdmin)
