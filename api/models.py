
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from stream_django import activity

# Create your models here.
class Catch(models.Model, activity.Activity):
	title = models.CharField(max_length=75)
	fishPhoto = models.ImageField(upload_to='photos/%Y/%m/%d')
	owner = models.ForeignKey('auth.User', related_name='catches')
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	def __unicode_(self):
		return self.title
		
	@property
	def activity_actor_attr(self):
		return self.owner
		
	@property
	def activity_object_attr(self):
		return self

	@property
	def activity_time_attr(self):
		return self.created_date

class Follow(models.Model):
	user = models.ForeignKey('auth.User', related_name='friends')
	target = models.ForeignKey('auth.User', related_name='followers')
	created_at = models.DateTimeField(auto_now_add=True)

	class Meta:
	    unique_together = ('user', 'target')

	
		
	
# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)