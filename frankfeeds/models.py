from django.db import models
import settings

class Project (models.Model):
	title       = models.CharField (max_length=512)
	description = models.XMLField ()
	skills      = models.XMLField ()
	site        = models.XMLField (blank=True)
	code        = models.XMLField ()
	#image       = models.ImageField (upload_to=settings.MEDIA_ROOT, blank=True)
	importance  = models.IntegerField (default=0, blank=True, null=True)

	def __str__ (self):
		return "Project - %s" % (self.title, )

class Snippet (models.Model):
	name    = models.CharField (max_length=128)
	snippet = models.XMLField ()
	
	def __str__ (self):
		return "Snippet - %s" % (self.name, )

class LatestBlog (models.Model):
    name    = models.CharField (max_length=128)
    title   = models.TextField ()
    summary = models.XMLField ()

    def __str__ (self):
        return "Blog - %s" % (self.title, )