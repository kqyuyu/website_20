from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('episodes/', views.episodes_list, name='episodes'),
    path('episodes/season/<int:season>/', views.episodes_list, name='episodes_by_season'),
    path('characters', views.home, name='characters'),
    path('news', views.home, name='news'),
    path('gallery', views.home, name='gallery'),
]
