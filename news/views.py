from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import News
from games.dict import platforms, genre, alphabet

def index(request):
    news= News.objects.all().order_by('-news_date')

    paginator = Paginator(news, 5)
    page = request.GET.get('page')
    paged_news = paginator.get_page(page)

    context ={
        'news': paged_news,
        'alphabet': alphabet,
        'genre': genre,
        'platform':platforms,
        
    }
    return render(request, 'news/news.html',context)


def news(request,news_id):
    news =  get_object_or_404(News,pk=news_id)

    context={
        'news': news,
        'alphabet': alphabet,
        'genre': genre,
        'platform':platforms,

        
    }
    return render(request, 'news/news_single.html', context)


def search_news(request):
    return render(request, 'reviews/reviews.html')


