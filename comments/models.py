from django.db import models
from catches.models import Catch
# Create your models here.



class Comment(models.Model):
	owner = models.ForeignKey('auth.User', related_name='commenter')
	created_at = models.DateTimeField(auto_now_add=True)
	target = models.ForeignKey('catches.Catch', related_name='comments')
	text = models.TextField(max_length=3000)
