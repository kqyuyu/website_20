from django.shortcuts import render
from django.core.paginator import Paginator
from datetime import datetime
from django.db.models import Max
from .models import Episode, News


def home(request):
    context = {
        'mythology_series': Episode.objects.filter(is_featured=True).order_by('air_date')[:8],
        'news_items': News.objects.order_by('-published_at')[:4],
        'featured_character': None,
        'current_year': datetime.now().year,
    }
    return render(request, 'home.html', context)


def episodes_list(request, season=None):
    """
    Отображает список эпизодов.
    Если передан season, фильтрует по сезону.
    """
    episodes_qs = Episode.objects.all().order_by('season', 'episode_number')

    if season is not None:
        episodes_qs = episodes_qs.filter(season=season)

    # Пагинация: 10 эпизодов на страницу
    paginator = Paginator(episodes_qs, 10)
    page_number = request.GET.get('page')
    episodes_page = paginator.get_page(page_number)

    # Для фильтра по сезонам — диапазон от 1 до максимального сезона
    max_season = Episode.objects.aggregate(max_season=Max('season'))['max_season'] or 11
    seasons_range = range(1, max_season + 1)

    context = {
        'episodes': episodes_page,
        'page_obj': episodes_page,
        'is_paginated': episodes_page.has_other_pages(),
        'seasons_range': seasons_range,
        'selected_season': season,  # для подсветки активного фильтра
    }
    return render(request, 'episodes.html', context)
