from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('', views.home, name='episodes'),
    path('', views.home, name='characters'),
    path('', views.home, name='news'),
    path('', views.home, name='gallery'),
]
