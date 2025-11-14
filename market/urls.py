from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_page, name='search_page'),  
    path('search/results/', views.search, name='search'),    
    path('sort/', views.sort_market, name='sort'),           
    path('match/', views.match_buyers, name='match'),        
    path('farmers/', views.farmers, name='farmers'),
]
