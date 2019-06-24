from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import Games
from .dict import alphabet,platforms,genre
from reviews.models import Reviews


def index(request):
    games= Games.objects.all().order_by('-posted_date')

    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)

    context ={
        'games': paged_games,
        'alphabet': alphabet,
        'platform': platforms,
        'genre': genre,
    }
    return render(request, 'games/games.html',context)


def game(request, game_id):
    game = get_object_or_404(Games, pk= game_id)
    review_single =Reviews.objects.filter(game=game_id)

    context={
        'game': game,
        'review': review_single
    }
    return render(request, 'games/game.html', context)

  
    


def searchByAlphabet(request,alpha):
    games= Games.objects.all().order_by("title").filter(title__startswith=alpha)
    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)

    context={
        'games': paged_games,
        'alphabet': alphabet,
        'platform': platforms,
        'genre': genre,
    }
    return render(request, 'games/games.html',context)

def searchByPlatform(request,plat):
    games= Games.objects.all().filter(platform__icontains=plat)
    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)

    context={
        'games':paged_games,
        'alphabet':alphabet,
        'platform':platforms,
        'genre':genre,
    }
    return render(request, 'games/search.html',context)

def searchByGenre(request,gen):
    games= Games.objects.all().filter(genre__icontains=gen)
    paginator = Paginator(games, 6)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)

    context={
        'games': paged_games,
        'alphabet': alphabet,
        'platform': platforms,
        'genre': genre,
    }
    return render(request, 'games/search.html',context)