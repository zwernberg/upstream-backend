
from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.
class Catch(models.Model):
	title = models.CharField(max_length=75)
	fishPhoto = models.ImageField()
	owner = models.ForeignKey('auth.User', related_name='catches')
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __unicode_(self):
		return self.title
		
	
# This code is triggered whenever a new user has been created and saved to the database
@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)