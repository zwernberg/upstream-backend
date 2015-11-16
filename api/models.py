
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class catch(models.Model):
	title = models.CharField(max_length=75)
	fishPhoto = models.ImageField(upload_to = 'fish_folder/')
	owner = models.ForeignKey('auth.User', related_name='catches')
	created_date = models.DateTimeField(auto_now_add=True)
	modified_date = models.DateTimeField(auto_now=True)

	def __unicode_(self):
		return self.title