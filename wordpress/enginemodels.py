import google.appengine.ext.db as db
from django.core.urlresolvers import reverse

class wp_posts (db.Model):
    ID = db.IntegerProperty()
    comment_count = db.IntegerProperty()
    comment_status = db.StringProperty()
    guid = db.StringProperty()
    post_author = db.IntegerProperty()
    post_content = db.TextProperty()
    post_date_gmt = db.DateTimeProperty()
    post_title = db.StringProperty()
    post_type = db.StringProperty()
    post_name = db.StringProperty()

    def get_absolute_url(self):
        year = self.post_date_gmt.year
        month = self.post_date_gmt.month
        day = self.post_date_gmt.day
        slug = self.post_name
        return reverse('wp_object_detail', args=(year, month, day, slug))
    
    @property
    def post_content_latin (self):
        return self.post_content.encode ('latin-1')

class wp_comments (db.Model):
    ID = db.IntegerProperty()
    comment_author = db.StringProperty()
    comment_author_email = db.StringProperty()
    comment_author_url = db.StringProperty()
    comment_content = db.TextProperty()
    comment_date_gmt = db.DateTimeProperty()
    comment_post_id = db.IntegerProperty()
    
    @property
    def comment_content_latin (self):
        return self.comment_content.encode ('latin-1')
