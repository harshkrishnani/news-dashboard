from django.urls import path
from .views import news_list, fetch_news_view

urlpatterns = [
    
    path('', news_list, name='news_list'),

    path('fetch/', fetch_news_view, name='fetch_news'),
]