from django.shortcuts import render
from django.http import HttpResponse
from games.dict import alphabet,platforms,genre
from games.models import Games
from news.models import News
from reviews.models import Reviews

def index(request):
    games=Games.objects.filter(is_trending=True)[:3]
    news= News.objects.order_by('-news_date')[:3]
    latest_game= Games.objects.order_by('-posted_date')[:1]
    latest_news= News.objects.order_by('-news_date')[:1]
    latest_reviews= Reviews.objects.order_by('-date')[:1]
    trending_news = News.objects.filter(is_trending=True)[:1]
    context={
        'alphabet':alphabet,
        'platform':platforms,
        'genre':genre,
        'games':games,
        'news': news,
        'latest_game':latest_game,
        'latest_news':latest_news,
        'latest_review':latest_reviews,
        'trending_news':trending_news,

    }
    return render(request, 'pages/index.html',context)

def contact(request):
    context={
        'alphabet': alphabet,
        'genre': genre,
        'platform':platforms,
    }
    return render(request, 'pages/contact.html',context)

def Search(request):
    queryset_list = Games.objects.order_by('-posted_date')
    keywords = request.GET['q']
    if keywords:
        queryset_list= queryset_list.filter(title__icontains=keywords)
    context={
        'games':queryset_list,
        'alphabet':alphabet,
        'genre':genre,
        'platform':platforms,
    }
    return render(request, 'games/search.html', context)