from django.core.management.base import BaseCommand
from news_fetcher.utils import fetch_news

class Command(BaseCommand):
    help = 'Fetches the latest news articles from the RSS feed.'

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting to fetch news articles...")
        fetch_news()
        self.stdout.write(self.style.SUCCESS('Successfully fetched and updated news articles.'))