from dataclasses import fields
import datetime
import feedparser
from django import forms
from django.contrib import admin
from django.forms import ValidationError

from news.models import Article, Feed

# Register your models here.

admin.site.register(Article)

# Admin overrides
class FeedForm(forms.ModelForm):
    class Meta:
        model = Feed
        fields = '__all__'
    
    def clean(self):
        feed = self.cleaned_data['url']
        feedExists = Feed.objects.filter(url = feed).exists()
        if feedExists:
            raise ValidationError('Feed already exists!')


class FeedAdmin(admin.ModelAdmin):
    form = FeedForm

    def save_model(self, request, obj, form, change): 
        if request.method == 'POST':
            form = FeedForm(request.POST) 
            if form.is_valid():
                feed =  form.save(commit=False)  
                feedData = feedparser.parse(feed.url)
                feed.title = feedData.feed.title
                feed.save()
                for entry in feedData.entries:
                    article = Article()
                    article.title = entry.title
                    article.url = entry.link
                    article.description = entry.description
                    try:
                        article.media = entry.media_content[0]['url']
                    except:
                        article.media = ''

                    article.author = entry.author
                    # published date formatting
                    d = datetime.datetime(*(entry.published_parsed[0:6]))
                    date = d.strftime('%Y-%m-%d %H:%M:%S')
                    article.publication_date = date
                    article.feed = feed
                    article.save()
        else:
            form = FeedForm

admin.site.register(Feed, FeedAdmin)
