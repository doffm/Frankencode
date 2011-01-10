from urllib2 import HTTPError
import twitter
import ttp
from django.core.cache import cache

from django.conf import settings

def latest_tweets (request):
    tweets = cache.get ("frankencode_tweets")
    if not tweets:
        tweets = []

    return {'tweets':tweets} 
