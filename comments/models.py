from django.db import models
from api.models import Catch
# Create your models here.



class Comment(models.Model):
	owner = models.ForeignKey('auth.User', related_name='commenter')
	created_at = models.DateTimeField(auto_now_add=True)
	target = models.ForeignKey('api.Catch', related_name='comments')
	text = models.TextField(max_length=3000)
