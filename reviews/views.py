from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import Reviews
from games.dict import platforms,genre,alphabet

def index(request):
    reviews= Reviews.objects.all().order_by('-date')

    paginator = Paginator(reviews, 5)
    page = request.GET.get('page')
    paged_reviews = paginator.get_page(page)

    context ={
        'reviews': paged_reviews,
        'alphabet':alphabet,
        'platform':platforms,
        'genre':genre,
    }
    return render(request, 'reviews/reviews.html',context)


def review_single(request, review_id):
    review_single = get_object_or_404(Reviews, pk= review_id)
 
    context={
        'review': review_single,
        'alphabet':alphabet,
        'platform':platforms,
        'genre':genre,
    } 
    return render(request, 'reviews/review_single.html',context)


def search_review(request):
    return render(request, 'reviews/reviews.html')


