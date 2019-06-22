from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name="reviews"),
    path('<int:review_id>', views.review, name="review"),
    path('search', views.search, name="search")
]
