from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('pages.urls')),
    path('games/', include('games.urls')),
    path('reviews/', include('reviews.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
