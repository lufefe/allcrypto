import datetime
from .models import Article, Feed
import feedparser
from django.shortcuts import render

class BackgroundClass:
    
    @staticmethod
    def update_db():
        
        # refresh server


        # Do your update db from RSS task here
        all_feeds = Feed.objects.all()
        # rss = feedparser.parse('https://www.coindesk.com/arc/outboundfeeds/rss/')
        # todo: figure out multi rss feed update logic
        rss = []
        for feed in all_feeds:
            print(feed.url)
            rss.append(feedparser.parse(feed.url))
        # rss = feedparser.parse(all_feeds.url)

        print(rss)
        already_updated = False
        for r in rss:
            first_entry = r.entries[0]
            print(first_entry)
        for slide in Article.objects.all():
            if first_entry.title == slide.title:
                already_updated = True
                print("already updated:", slide)
    
        print(already_updated)
        if not already_updated:
            print("not already_updated")
            for entry in rss.entries:
                print(entry.title_detail.base)
                
                get_feed_id = Feed.objects.get(url = entry.title_detail.base)
                print(get_feed_id)
  
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
                article.feed = get_feed_id
                article.save()


    # def test(request):
    #     articles = Article.objects.all()
    #     slides = Slide.objects.all()
    #     return render(request, 'sample/test_amp.html', {'articles':articles, 'slides':slides})