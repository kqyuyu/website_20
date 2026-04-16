from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def home(request):
    context = {
        'latest_episodes': [],
        'news_items': [],
        'featured_character': None,
        'current_year': datetime.now().year,
    }
    return render(request, 'home.html', context)
