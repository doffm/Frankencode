
import settings
import feedparser

from models import LatestBlog

LATEST_BLOG_ID = 'latestblog'

def __update (snp):
    feed = feedparser.parse (settings.BLOG_FEED)
    latest = feed.entries[0]
    
    snp.name = LATEST_BLOG_ID
    snp.title = latest.title
    snp.summary = latest.summary
    snp.save()

def invalidateBlog ():
    cached = LatestBlog.objects.filter (name=LATEST_BLOG_ID)

    if (len (cached) > 0):
        snp = cached[0]
    else:
        snp = LatestBlog ()
        
    __update (snp)

def getBlog ():
    cached = LatestBlog.objects.filter (name=LATEST_BLOG_ID)

    if (len (cached) > 0):
        snp = cached[0]
    else:
        snp = LatestBlog ()
        __update (snp)

    return snp
