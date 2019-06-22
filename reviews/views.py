from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import Reviews


def index(request):
    reviews= Reviews.objects.all().order_by('-date')

    paginator = Paginator(reviews, 2)
    page = request.GET.get('page')
    paged_reviews = paginator.get_page(page)

    context ={
        'reviews': paged_reviews
    }
    return render(request, 'reviews/reviews.html',context)


def review(request, game_id):
    return render(request, 'reviews/review.html')


def search(request):
    return render(request, 'reviews/reviews.html')


