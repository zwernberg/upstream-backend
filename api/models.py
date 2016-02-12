
from django.db import models
from django.db.models import signals
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from stream_django import activity
from stream_django.feed_manager import feed_manager


# Create your models here.

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
		
def unfollow_feed(sender, instance, **kwargs):
    feed_manager.unfollow_user(instance.user_id, instance.target_id)

def follow_feed(sender, instance, created, **kwargs):
    if created:
        feed_manager.follow_user(instance.user_id, instance.target_id)


signals.post_delete.connect(unfollow_feed, sender=Follow)
signals.post_save.connect(follow_feed, sender=Follow)