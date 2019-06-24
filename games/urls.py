from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name="games"),
    path('<int:game_id>', views.game, name="game"),
    path('<str:alpha>', views.searchByAlphabet, name="game_alpha"),
    path('search/<str:plat>', views.searchByPlatform, name="game_plat"),
    path('search1/<str:gen>', views.searchByGenre, name="game_gen"),


]