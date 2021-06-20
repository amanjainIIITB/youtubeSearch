from django.db import models

# Create your models here.

class ContentDetails(models.Model):
    videoID = models.CharField(max_length=15, default=None)
    publishedAt = models.DateTimeField()
    title = models.CharField(max_length=500)
    description = models.CharField(max_length=1000)
    thumbnail_url = models.URLField()

    def __str__(self):
        return self.title