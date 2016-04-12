from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User)
	
	#custom userProfile Fields
	bio = models.TextField(default='', blank=True)



#Signals
def create_profile(sender, **kwargs):
	user = kwargs["instance"]
	if kwargs["created"]:
		up = UserProfile(user=user)
		up.save()
post_save.connect(create_profile, sender=User)