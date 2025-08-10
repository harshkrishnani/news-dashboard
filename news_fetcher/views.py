from django.shortcuts import render, redirect
from .models import NewsArticle
from .utils import fetch_news

def news_list(request):
    """
    This view fetches all articles from the database and
    sends them to the template to be displayed.
    """
    articles = NewsArticle.objects.all().order_by('-published_at')
    return render(request, 'news_fetcher/news_list.html', {'articles': articles})

def fetch_news_view(request):
    """
    This view is called when the 'Fetch Latest News' button is clicked.
    It runs the fetch_news function and then redirects back to the main list.
    """
    if request.method == 'POST':
        fetch_news()
    return redirect('news_list')