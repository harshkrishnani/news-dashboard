import feedparser
from dateutil import parser
from .models import NewsArticle

def fetch_news():
    feed = feedparser.parse("https://news.google.com/rss")

    for entry in feed.entries:
        if not NewsArticle.objects.filter(title=entry.title).exists():
            NewsArticle.objects.create(
                title=entry.title,
                summary=entry.summary,
                source=entry.source.title if hasattr(entry, 'source') else 'N/A',
                published_at=parser.parse(entry.published)
            )