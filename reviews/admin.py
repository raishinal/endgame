from django.contrib import admin
from .models import Reviews


class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('id','title','ratings','date','game')
    list_display_links = ('id','title')
    search_fields = ('title',)
    list_editable = ('ratings',)


admin.site.register(Reviews,ReviewsAdmin)
