from django.db import models

class NewsArticle(models.Model):
    title = models.CharField(max_length=200, unique=True)
    summary = models.TextField(blank=True, null=True)
    source = models.CharField(max_length=100) 
    published_at = models.DateTimeField() 

    def __str__(self):
        return self.title