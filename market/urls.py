from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search, name='search'),
    path('sort/', views.sort_market, name='sort'),
    path('match/', views.match_buyers, name='match'),
]
