from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255,null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    url = models.URLField(max_length=200,null=True, blank=True)
    published_at = models.DateTimeField(null=True, blank=True)
    source_name = models.CharField(max_length=100,null=True, blank=True)

