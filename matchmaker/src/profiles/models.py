from __future__ import unicode_literals

from django.db import models
from django.conf import settings 

# Create your models here.

User = settings.AUTH_USER_MODEL


def upload_location(instance, filename):
	#extension = filename.split(".")
	location = str(instance.user.username)
	return "%s/%s" % (location, extension)


class Profile(models.Model):
	user = models.OneToOneField(User)
	location = models.CharField(max_length = 20, null = True, blank = True)
	picture = models.ImageField(upload_to = upload_location, null = True, blank = True)


	def __unicode__(self): 
		return self.user.username
