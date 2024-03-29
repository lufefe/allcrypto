import datetime
from django.shortcuts import render
from news.forms import FeedForm
from django.shortcuts import redirect
from news.models import Article, Feed

# Create your views here.
# todo : enhance logic by using one object to store multiple feeds; use random numbers to assign feeds from database.
def articles_list(request): #todo update feeds and numbers in objects.filter statement
    # Source 1 - https://www.coindesk.com/arc/outboundfeeds/rss/
    articles1 = Article.objects.filter(feed = 21).order_by('-publication_date')
    rows1 = [articles1[x:x+1] for x in range(0, len(articles1), 1)]

    # Source 2 - https://cointelegraph.com/rss
    articles2 = Article.objects.filter(feed = 22).order_by('-publication_date')
    rows2 = [articles2[x:x+1] for x in range(0, len(articles2), 1)]

    # Source 3 - https://crypto.news/feed/
    articles3 = Article.objects.filter(feed = 23).order_by('-publication_date')
    rows3 = [articles3[x:x+1] for x in range(0, len(articles3), 1)]

    # Source 4 - https://coinstats.app/blog/feed/ [24]|| https://bitcoinist.com/feed/ [26]
    articles4 = Article.objects.filter(feed = 26).order_by('-publication_date')
    rows4 = [articles4[x:x+1] for x in range(0, len(articles4), 1)]

    # Source 5 - Podcast
    
    return render(request, 'articles_list.html', {'rows1': rows1, 'rows2': rows2, 'rows3': rows3, 'rows4': rows4})

def feeds_list(request):
    feeds = Feed.objects.all()
    return render(request, 'feeds_list.html', {'feeds': feeds})

def contactus(request):
    return render(request, 'contact_us.html')

def privacypolicy(request):
    return render(request, 'privacy_policy.html')
