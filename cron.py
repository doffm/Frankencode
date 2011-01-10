import os
import sys

# Add parent folder to sys.path, so we can import boot.
# App Engine causes main.py to be reloaded if an exception gets raised
# on the first request of a main.py instance, so don't add project_dir multiple
# times.
project_dir = os.path.abspath(os.path.dirname(__file__))
if project_dir not in sys.path or sys.path.index(project_dir) > 0:
    sys.path.insert(0, project_dir)

# Remove the standard version of Django.
if 'django' in sys.modules and sys.modules['django'].VERSION < (1, 2):
    for k in [k for k in sys.modules
              if k.startswith('django\.') or k == 'django']:
        del sys.modules[k]

from djangoappengine.boot import setup_env, setup_logging, env_ext
setup_env()

# ------------------

from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

from urllib2 import HTTPError
import twitter
import ttp
from django.core.cache import cache

from django.conf import settings
from frankfeeds.latestblog import invalidateBlog

class TweetsUpdate(webapp.RequestHandler):
    def get(self):
        try:
            tweets = twitter.Api().GetUserTimeline (settings.TWITTER_USER, settings.TWITTER_TWEETS)
            p = ttp.Parser ()
            for tweet in tweets:
                tweet.html = p.parse (tweet.text).html
                tweet.date = tweet.created_at[:-11]
            cache.set ("frankencode_tweets", tweets, 60 * 60 * 8)
        except HTTPError:
            pass

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('')

class BlogUpdate(webapp.RequestHandler):
    def get(self):
        invalidateBlog ()

        self.response.headers['Content-Type'] = 'text/plain'
        self.response.out.write('')

application = webapp.WSGIApplication(
                                     [('/tasks/update/tweets', TweetsUpdate),
                                      ('/tasks/update/blog', BlogUpdate)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()
