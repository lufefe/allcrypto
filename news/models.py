from django.db import models

# Create your models here.

class Feed(models.Model):
    title = models.CharField(max_length=500)
    url = models.URLField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Article(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    url = models.URLField()
    media = models.URLField(default=None)
    description = models.TextField()
    publication_date = models.DateTimeField()
    author = models.CharField(max_length=500)

    def __str__(self):
        return self.title