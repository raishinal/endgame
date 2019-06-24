from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name="reviews"),
    path('<int:review_id>', views.review_single, name="review_single"),
    path('searchreview', views.search_review, name="search_review")
]
