from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import News


def index(request):
    news= News.objects.all().order_by('-news_date')

    paginator = Paginator(news, 2)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)

    context ={
        'news': paged_news
    }
    return render(request, 'news/news.html',context)


def news(request, game_id):
    return render(request, 'news/news_single.html')


def search(request):
    return render(request, 'reviews/reviews.html')


