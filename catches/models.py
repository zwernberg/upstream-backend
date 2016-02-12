from django.db import models
from django.contrib.auth.models import User
from stream_django import activity
from stream_django.feed_manager import feed_manager

# Create your models here.
class Catch(models.Model, activity.Activity):
	title = models.CharField(max_length=75)
	fishPhoto = models.ImageField(upload_to='photos/%Y/%m/%d')
	owner = models.ForeignKey('auth.User', related_name='catches')
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)
	likes = models.IntegerField(default=0)


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



class Like(models.Model):
	user = 	models.ForeignKey('auth.User')
	catch = models.ForeignKey('Catch', related_name='liked_users')
	created_at = models.DateTimeField(auto_now_add=True)	
	
	class Meta:
		unique_together = ('user', 'catch')