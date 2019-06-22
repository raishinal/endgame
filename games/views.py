from django.shortcuts import get_object_or_404,render
from django.core.paginator import EmptyPage, PageNotAnInteger , Paginator
from .models import Games


def index(request):
    games= Games.objects.all().order_by('-posted_date')

    paginator = Paginator(games, 2)
    page = request.GET.get('page')
    paged_games = paginator.get_page(page)

    context ={
        'games': paged_games
    }
    return render(request, 'games/games.html',context)


def game(request, game_id):
    game = get_object_or_404(Games, pk= game_id)

    context={
        'game': game
    }
    return render(request, 'games/game.html', context)


def search(request):
    return render(request, 'games/games.html')


