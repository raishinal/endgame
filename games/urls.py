from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name="games"),
    path('<int:game_id>', views.game, name="game"),
    path('search', views.search, name="search")
]