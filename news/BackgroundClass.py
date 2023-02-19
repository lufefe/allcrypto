import datetime
from .models import Article, Feed
import feedparser
from django.shortcuts import render

class BackgroundClass:
    
    @staticmethod
    def update_db():
        # refresh server here
        print("Updating ...")
        # Do your update db from RSS task here
        all_feeds = Feed.objects.all()
        rss = []
        for feed in all_feeds:
            rss.append(feedparser.parse(feed.url))

        already_updated = False
        for r in rss:
            for ent in r.entries:
                # print(ent.title, ent.published)
                for art in Article.objects.all():
                    if ent.title == art.title:
                        already_updated = True
                    else:
                        get_feed_id = Feed.objects.get(url = article.title_detail.base)

                        article = Article()
                        article.title = artitle.title
                        article.url = artitle.link
                        article.description = artitle.description
                        try:
                            article.media = artitle.media_content[0]['url']
                        except:
                            article.media = ''

                        article.author = artitle.author
                        # published date formatting
                        d = datetime.datetime(*(artitle.published_parsed[0:6]))
                        date = d.strftime('%Y-%m-%d %H:%M:%S')
                        article.publication_date = date
                        article.feed = get_feed_id
                        article.save()
                        print("Articles updated -", date)
                        
    

    # def test(request):
    #     articles = Article.objects.all()
    #     slides = Slide.objects.all()
    #     return render(request, 'sample/test_amp.html', {'articles':articles, 'slides':slides})
